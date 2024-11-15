from machine import Pin
from gpio_lcd import GpioLcd

# instans af LCD objekt
lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25), d4_pin=Pin(33), d5_pin=Pin(32), d6_pin=Pin(21), d7_pin=Pin(22), num_lines=4, num_columns=20)

# Husk at LCD er 0-indekseret
lcd.clear() # Metoden clear rydder display for eventuelt tekst der allerede vises
lcd.move_to(0,0) # Metoden move_to flytter markøren til 1. kolonne på linje 1
mit_navn="Nicolai M" # Man kan også benytte variabel og f-string literals
lcd.putstr(f'{mit_navn}')

lcd.move_to(0,0)
lcd.blink_cursor_on() # Blink markøren

