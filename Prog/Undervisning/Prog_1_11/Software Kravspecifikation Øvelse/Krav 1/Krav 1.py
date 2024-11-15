"""
Lav et PWM objekt som er tilknyttet GPIO 13 og navngiv det lcd_brightness sæt duty cycle til 0.
Prøv at omskrive det så at rotary encoder anvendes til at skrue op og ned for lysintensiteten på LCD displayet. 
Der må som sagt max være 10 forskellige lysintensiteter. (Husk at duty som default er en 10 Bit værdi)
"""

from machine import Pin, PWM

# CONFIGURATION
# Rotary encoder pins, actual A or B depends the rotary encoder hardware. If backwards swap the pin numpers
pin_enc_a = 36
pin_enc_b = 39
lcd_brightness=PWM(Pin(13,Pin.OUT),duty=0)

# OBJECTS
rotenc_A = Pin(pin_enc_a, Pin.IN, Pin.PULL_UP)
rotenc_B = Pin(pin_enc_b, Pin.IN, Pin.PULL_UP)


# VARIABLES and CONSTANTS
enc_state = 0                          # Encoder state control variable

counter = 0                            # A counter that is incremented/decremented vs rotation

CW = 1                                 # Constant clock wise rotation
CCW = -1                               # Constant counter clock wise rotation


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
        if counter>10:
            counter=10
            lcd_brightness.duty(int(1023/10*counter))
        else:
            lcd_brightness.duty(int(1023/10*counter))
        print(counter)
    elif res == CCW:
        if counter<=1:
            counter=0
            lcd_brightness.duty(int(1023/10*counter))
        else:
            lcd_brightness.duty(int(1023/10*counter))
        print(counter)
