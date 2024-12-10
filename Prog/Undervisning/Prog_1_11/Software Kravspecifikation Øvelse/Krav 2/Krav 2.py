"""
Upload følgende to moduler til lib mappen på ESP32: 
https://github.com/KEA-IT-TEKNOLOG/ittek/blob/main/lib/lcd_api.py 
https://github.com/KEA-IT-TEKNOLOG/ittek/blob/main/lib/gpio_lcd.py 

Betragt kodeeksemplet med LCD https://github.com/KEA-IT-TEKNOLOG/ittek/blob/main/examples/lcd.py 

Betragt kodeeksemplet med batteri demo 
https://github.com/KEA-IT-TEKNOLOG/ittek/blob/main/examples/batt_demo_using_pot.py 

Prøv at lave en ny fil og brug delene fra de to ove
"""

from machine import Pin, PWM
from gpio_lcd import GpioLcd
from time import ticks_ms, ticks_diff

# CONFIGURATION
# Rotary encoder pins, actual A or B depends the rotary encoder hardware. If backwards swap the pin numpers
pin_enc_a = 36
pin_enc_b = 39

# OBJECTS
rotenc_A = Pin(pin_enc_a, Pin.IN, Pin.PULL_UP)
rotenc_B = Pin(pin_enc_b, Pin.IN, Pin.PULL_UP)
lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25), d4_pin=Pin(33), d5_pin=Pin(32), d6_pin=Pin(21), d7_pin=Pin(22), num_lines=4, num_columns=20)


# VARIABLES and CONSTANTS
enc_state = 0                          # Encoder state control variable

counter = 0                            # A counter that is incremented/decremented vs rotation

CW = 1                                 # Constant clock wise rotation
CCW = -1                               # Constant counter clock wise rotation

ticker=ticks_ms()

# FUNCTIONS
# Rotary encoder truth table, which one to use depends the actual rotary encoder hardware


def re_full_step():
    global enc_state

    encTableFullStep = [
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

# PROGRAM
print("Rotary encoder test program\n")
        
while True:
    # Read the rotary encoder
    res = re_full_step()               # or: re_half_step()

    # Direction and counter
    counter += res
    if res == CW:
        if counter>99:
            counter=100
    elif res == CCW:
        if counter<1:
            counter=0
    if ticks_diff(ticks_ms(),ticker)>2000:
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr(f"{counter}% batteri")
        ticker=ticks_ms()