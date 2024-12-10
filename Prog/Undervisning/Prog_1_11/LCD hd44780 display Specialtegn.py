from machine import Pin
from gpio_lcd import GpioLcd

# Instans af LCD objekt
lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25), d4_pin=Pin(33), d5_pin=Pin(32), d6_pin=Pin(21), d7_pin=Pin(22), num_lines=4, num_columns=20)

lcd.clear() # Ryd display for eventuely tekst der allerede vises

# Opret custom karakter
custom_chr = bytearray([
    0b00111,
    0b00101,
    0b00111,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000])

lcd.putstr('Temperatur: 10 C')
# Ryk markøren så den er mellem 10 og C
lcd.move_to(14,0) # 15.kolonne i 1. linje
# 1. argument er pladsen i CGRAM hukommelsen på LCD, man kan give integer 0-7
lcd.custom_char(0,custom_chr)
# Skriver angivne tegn til LCD og den nuværende markør på pladsen 1 kolonne frem
lcd.putchar(chr(0))