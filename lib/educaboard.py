""" A collection of my most frequently used instantiations for the educaboard. """

import hw
from gpio_lcd import GpioLcd
from machine import Pin


""" The following section is for the educaboard lcd. """
def inst_lcd():
    """ Instantiate the educaboard lcd. """
    return GpioLcd(rs_pin=Pin(hw.pin_lcd_rs),
    enable_pin=Pin(hw.pin_lcd_enable),
    d4_pin=Pin(hw.pin_lcd_db4),
    d5_pin=Pin(hw.pin_lcd_db5),
    d6_pin=Pin(hw.pin_lcd_db6),
    d7_pin=Pin(hw.pin_lcd_db7),
    num_lines=hw.lcd_num_lines,
    num_columns=hw.lcd_num_columns)

def lcd_write(lcd_name,string_parameter,col=0,row=0):
    if isinstance(string_parameter,str):
        lcd_name.move_to(col,row)
        lcd_name.putstr("                  ")
        lcd_name.move_to(col,row)
        lcd_name.putstr(str(string_parameter))
    else:
        print("Please enter a valid string.")

def lcd_write(self,string_parameter,col=0,row=0):
    if isinstance(str,string_parameter):
        self.move_to(col,row)
        self.putstr("                  ")
        self.move_to(col,row)
        self.putstr(str(string_parameter))
    else:
        print("Please enter a valid string.")