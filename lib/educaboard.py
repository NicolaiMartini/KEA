"""
A collection of my frequently used classed and functions for my Educaboard
"""
import hw
from gpio_lcd import GpioLcd
from machine import PWM, Pin


"""
The following section is for any classes and functions specifically for the LCD
"""
class lcd():
    """ Quickly instantiate LCD from educaboard. """
    def __init__(self):
        self.rs_pin=hw.pin_lcd_rs
        self.enable_pin=hw.pin_lcd_enable
        self.d4_pin=hw.pin_lcd_db4
        self.d5_pin=hw.pin_lcd_db5
        self.d6_pin=hw.pin_lcd_db6
        self.d7_pin=hw.pin_lcd_db7
        self.num_lines=hw.lcd_num_lines
        self.num_columns=hw.lcd_num_columns
        # pin to control lcd-brightness from hw.py, instantiated by Pin(), and turned into a controllable PWM
        self.pwm=PWM(Pin(hw.pin_portexp_mosi,Pin.OUT),duty=0)
        
    """ Adjust brightness in steps from 1 to 10 (0 to 9). """
    def bright(self,counter):
        duty=int(counter*102.3)
        return self.pwm.duty(duty)
    

"""
The following section is for any classes and functions for the RE (Rotary Encoder)
"""
class rotary_encoder():
    """ Quickly instantiate RE from educaboard. """
    def __init__(self):
        self.pin_a=Pin(hw.pin_enc_b,Pin.IN,Pin.PULL_UP)
        self.pin_b=Pin(hw.pin_enc_a,Pin.IN,Pin.PULL_UP)
        self.enc_state=0
        self.counter=0
        self.CW=1
        self.CCW=-1
        self.re_ticks=ticks_ms()
        
    """ RE table """
    def re_full_step(self):
        enc_state=self.enc_state
        
        encTableFullStep=[
            [0x00, 0x02, 0x04, 0x00],
            [0x03, 0x00, 0x01, 0x10],
            [0x03, 0x02, 0x00, 0x00],
            [0x03, 0x02, 0x01, 0x00],
            [0x06, 0x00, 0x04, 0x00],
            [0x06, 0x05, 0x00, 0x20],
            [0x06, 0x05, 0x04, 0x00]]

        enc_state = encTableFullStep[enc_state & 0x0F][(self.pin_b.value() << 1) | self.pin_a.value()]
    
        # result ændrer sig ALDRIG?? Wtf??
        result = enc_state & 0x30
        if (result==0x10):
            return self.CW
        elif (result==0x20):
            return self.CCW
        else:
            return 0
        
# "result" skal opdatere før nedenstående kan viderearbejdes på
#     def re_counter(self):
#         re_counter=self.counter
#         if ticks_ms()-self.re_ticks>50:
#             re_counter+=self.re_full_step()
#             print(re_counter)
#             self.re_ticks=ticks_ms()
#             return re_counter
