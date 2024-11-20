from time import ticks_ms, ticks_diff
from machine import reset, ADC, Pin, PWM
# from client import TBDevice MqttClient
import gc
import secrets


ticker=ticks_ms() # Initiate non-blocking delay ticker

# Pins
potmeter_adc=ADC(Pin(34))
potmeter_adc.atten(ADC.ATTN_11DB)

### 
# Battery functions
# Linear function for batt-% calculations
adc1=2390
U1=4.1
adc2=2080
U2=3.6
a=(U1-U2)/(adc1-adc2)
b=U2-a*adc2

# Batt % based on voltage
# 3V = 0%
# 4.2V = 100%
def batteri_percent():
    val=potmeter_adc.read() # Read potmeter
    u_batt=a*val+b # Linear calc
    without_offset=(u_batt-3)
    normalized=without_offset/(4.2-3.0) # Normalize
    percent=normalized*100 # Return in percentage
    
# Thingsboard connection
###
# client=TBDeviceMqttClient(secrets.SERVER_IP_ADDRESS, access_token=secrets.ACCESS_TOKEN)
# client.connect() # Connecting to Thingsboard
print("Connected to thingsboard, starting to send and receive data.")

# Main program
while True:
    try:
        if ticks_diff(ticks_ms(),ticker)>1000: # 5s non-blocking delay
            print(f"free memory: {gc.mem_free()}") # monitor memory left
            print(batteri_percent())                # store telemetry in dictionary     
            telemetry={"Batteri Percentage":batteri_percent()} # Storing telemetry in dictionary
#              client.send_telemetry(telemetry) # Sending telemetry to Thingsboard
            ticker=ticks_ms()
    except KeyboardInterrupt:
        print("Disconnected!")
#         client.disconnect()               # Disconnecting from ThingsBoard
        reset()                           # reset ESP32

