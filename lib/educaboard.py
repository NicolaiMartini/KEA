""" A collection of my frequently used classed and functions for my Educaboard. """
import hw
from gpio_lcd import GpioLcd
from machine import PWM, Pin
from neopixel import NeoPixel
from time import ticks_ms


""" The following section is for any classes and functions specifically for the LCD ."""
class Lcd():
    """ Quickly instantiate LCD on the Educaboard. """
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
    def bright(counter):
        duty=int(counter*102.3)
        return self.pwm.duty(duty)
    

""" The following section is for any classes and functions for the RE (Rotary Encoder). """
class RotaryEncoder():
    """ Quickly instantiate RE on the educaboard. """
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

""" The following section is for any classes and functions for the red LED. """
class RedLed():
    """ Quickly instantiate Red LED on the Educaboard. Active high. """
    def __init__(self):
        self.pin=Pin(hw.pin_led1, Pin.IN)
        self.pin.value(0)

    def red_steady_blink_ms(self,red_tick_var,red_tick_threshold):
        """ Predefined variable for blinking the LED steadily. Provide the named tick_variable and a ticks_ms threshold. E.G. tick_var named "x_ticker_led" and threshold named "x_ticker_led_threshold". """
        if ticks_ms()-red_tick_var>red_tick_threshold:
            self.pin.value(not self.pin.value())


""" The following section is for any classes and functions for the yellow LED. """
class YellowLed():
    """ NOT MADE YET.
    Quickly instantiate Yellow LED on Educaboard. Active low. """
    def __init__(self):
        self.pin=Pin(12,Pin.OUT) # Pin 12, Port exp. has to be bypassed by JP1-MISO<->JP6-G-2 
        self.pin.value(1)
    
    def yellow_steady_blink_ms(self,yellow_tick_var,yellow_tick_threshold):
        """ Predefined variable for blinking the LED steadily. Provide the named tick_variable and a ticks_ms threshold. E.G. tick_var named "x_ticker_led" and threshold named "x_ticker_led_threshold". """
        if ticks_ms()-yellow_tick_var>yellow_tick_threshold:
            self.pin.value(not self.pin.value())


""" The following section is for any classes and functions for the green LED. """
class GreenLed():
    """ NOT MADE YET. 
    Quickly instantiate the Green LED on the Educaboard. Active high. """
    def __init__(self):
        self.pin=Pin(13,Pin.OUT) # Pin 13, Port exp. has to be bypassed by JP1-MOSI<->JP6-GP2
        self.pin.value(0)
    
    def green_steady_blink_ms(self,green_tick_var,green_tick_threshold):
        """ Predefined variable for blinking the LED steadily. Provide the named tick_variable and a ticks_ms threshold. E.G. tick_var named "x_ticker_led" and threshold named "x_ticker_led_threshold". """
        if ticks_ms()-green_tick_var>green_tick_threshold:
            self.pin.value(not self.pin.value())


""" The following section is for any classes and functions for the. """
class Potmeter():
    """ NOT TESTED YET. 
    Quickly instantiate the potmeter on the Educaboard. Defaults are: ATTN_11DB and WIDTH_12BIT. """
    def __init__(self):
        self.adc=ADC(Pin(hw.pin_potmeter,Pin.IN))
        self.atten=ADC.ATTN_11DB
        self.width=ADC.WIDTH_12BIT


""" The following section is for any classes and functions for the. """
class NeoPixelRing(np_pin=12,np_amount=12):
    """ NOT MADE YET.
    Quickly instantiate the NeoPixelRing that can be attached to the Educaboard. """
    def __init__(self):
        self.np=NeoPixel(Pin(np_pin,Pin.OUT),np_amount) # NPR should be connected to pin 12 by default, and it contains 12 neopixels


""" The following section is for any classes and functions for the PushButton 1 on the Educaboard. """
class PB1():
    """ NOT MADE YET.
    Quickly instantiate the PB1 on the Educaboard.""" 
    def __init__(self):
        self.pin=Pin(hw.pb1,Pin.IN)

    # See if I can make a predefined debounce function?
    pb1_debounce():
        while True:
            PB1_debounce_ticker=ticks_ms()
            first=PB1.value()
            if ticks_ms()-PB1_debounce_ticker>10:
                second=PB1.value()
                break
        


""" The following section is for any classes and functions for the """