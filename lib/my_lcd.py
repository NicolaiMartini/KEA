"""
A collection of my frequently used functions for my Educaboard Liquid Crystal Display
"""

# Can this work without the following 2 imports?
# from machine import Pin
# from lcd_api import LcdApi
from gpio_lcd import GpioLcd
import hw

def educaboard_lcd():
    return GpioLcd(rs_pin=hw.pin_lcd_rs, enable_pin=hw.pin_lcd_enable, d4_pin=hw.pin_lcd_db4, d5_pin=hw.pin_lcd_db5, d6_pin=hw.pin_lcd_db6, d7_pin=hw.pin_lcd_db7, num_lines=hw.lcd_num_lines, num_columns=hw.lcd_num_columns)


def lcd_write(parameter,col=0,row=0):
    """ Insert string to write to display. Default col and row is (0,0), but can be overridden. """
    if isinstance(parameter,str): # Check to make sure "parameter" is a string
        lcd.move_to(col,row)
        lcd.putstr(" "*(len(parameter)+1))
        lcd.move_to(col,row)
        lcd.putstr(parameter)
    else:
        print("Argument has to be a string. Try again")

def lcd_brightness_10(counter,duty=0):
    """ Set duty of LC-display. Steps from 0 to 10. """
    counter=int(counter)
    lcd.duty(counter*102.3)
    # return lcd.duty(int(counter*102.3)) # Do i need to return it?