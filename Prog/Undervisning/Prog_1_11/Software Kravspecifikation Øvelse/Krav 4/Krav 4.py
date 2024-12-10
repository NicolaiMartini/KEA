from machine import Pin, PWM, ADC, reset
from time import ticks_ms, ticks_diff
from gpio_lcd import GpioLcd
from uthingsboard.client import TBDeviceMqttClient
import gc
import secrets
import dht

# PINS
pin_enc_b=39
pin_enc_a=36
potmeter_pin=34
dht11_pin=19
lcd_pin=13

#####
# OBJECTS
rotenc_A=Pin(pin_enc_a,Pin.IN,Pin.PULL_UP)
rotenc_B=Pin(pin_enc_b,Pin.IN,Pin.PULL_UP)
lcd_brightness=PWM(Pin(lcd_pin,Pin.OUT),duty=0)
lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25), d4_pin=Pin(33), d5_pin=Pin(32), d6_pin=Pin(21), d7_pin=Pin(22), num_lines=4, num_columns=20)
potmeter_adc=ADC(Pin(potmeter_pin))
potmeter_adc.atten(ADC.ATTN_11DB)
dht11=dht.DHT11(Pin(dht11_pin))

#####
# VARIABLES AND CONSTANTS
enc_state=0 # Encoder state control variable
counter=0 # A counter that is in-/decremented vs rotation
CW=1 # Constant clock wise rotation
CCW=-1 # Constant counter clock wise rotation
ticker_lcd=ticks_ms()
ticker_thingsboard=ticks_ms()
ticker_dht11=ticks_ms()

# Linear functions for Battery%-calculation
adc1=2390
U1=4.1
adc2=2080
U2=3.6
a=(U1-U2)/(adc1-adc2)
b=U2-a*adc2

##### FUNCTIONS
# ROTARY ENCODER
def re_full_step():
    global enc_state

    encTableFullStep=[
        [0x00, 0x02, 0x04, 0x00],
        [0x03, 0x00, 0x01, 0x10],
        [0x03, 0x02, 0x00, 0x00],
        [0x03, 0x02, 0x01, 0x00],
        [0x06, 0x00, 0x04, 0x00],
        [0x06, 0x05, 0x00, 0x20],
        [0x06, 0x05, 0x04, 0x00]]

    enc_state = encTableFullStep[enc_state & 0x0F][(rotenc_B.value() << 1) | rotenc_A.value()]

    # -1: Left/CCW, 0: No rotation, 1: Right/CW
    result = enc_state & 0x30
    if (result == 0x10):
        return CW
    elif (result == 0x20):
        return CCW
    else:
        return 0
    
# IN-/DECREASE LC-DISPLAY
def adjust_lcd_brightness():
    global counter
    global lcd_duty
    lcd_duty=int(1023/10*counter)
    return lcd_brightness.duty(lcd_duty)

# Batt % based on voltage
# 3V = 0%
# 4.2V = 100%
def batteri_percent():
    val=potmeter_adc.read() # Read potmeter
    u_batt=a*val+b # Linear calc
    without_offset=(u_batt-3)
    normalized=without_offset/(4.2-3.0) # Normalize
    percent=normalized*100 # Return in percentage
    return percent

# Return Celsius, C
def dht11_temp():
    dht11.measure()
    tempC=dht11.temperature()
    temperature=f"{tempC}°C"
    return temperature

# Return Humidity, %
def dht11_hum():
    dht11.measure()
    hum=dht11.humidity()
    humidity=f"{hum}%"
    return humidity


#####
# Thingsboard connection
client=TBDeviceMqttClient(secrets.SERVER_IP_ADDRESS, access_token=secrets.ACCESS_TOKEN)
client.connect() # Connecting to Thingsboard
print("Connected to thingsboard, starting to send and receive data.")

#####
# Main Program
while True:
    try:
        if gc.mem_free() < 2000:          # free memory if below 2000 bytes left
            print("Garbage collected!")
            gc.collect()
        res = re_full_step() # Read rotary encoder
        counter+=res # In-/Decrease counter by RE
        counter=min(max(counter,0),10) # Max 10, Min 0
        adjust_lcd_brightness() # Call function to adjust brightness
        if ticks_diff(ticks_ms(),ticker_lcd)>2000:
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr(f"Battery: {batteri_percent()}%")
            lcd.move_to(0,1)
            lcd.putstr(f"Brightness: {counter} of 10")
            ticker_lcd=ticks_ms() # "Reset" non-blocking delay
        if ticks_diff(ticks_ms(),ticker_dht11)>10000:
            print(dht11_temp())
            print(dht11_hum())
            ticker_dht11=ticks_ms()
        if ticks_diff(ticks_ms(),ticker_thingsboard)>20000:
            telemetry={"Batteri Percentage":batteri_percent(),"Temperature":dht11_temp,"Humidity" : dht11_hum(),} # Store data in telemetry for Thingsboard
            print("Sending Telemetry") # Print when sending data
            client.send_telemetry(telemetry) # Send telemetry to Thingsboard
            ticker_thingsboard=ticks_ms() # "Reset" non-blocking delay
    except KeyboardInterrupt:
        print("Disconnected!")
        client.disconnect()               # Disconnecting from ThingsBoard
        reset()                           # reset ESP32
