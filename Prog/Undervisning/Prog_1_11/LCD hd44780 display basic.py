from machine import Pin
from gpio_lcd import GpioLcd

# instans af LCD objekt
lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25), d4_pin=Pin(33), d5_pin=Pin(32), d6_pin=Pin(21), d7_pin=Pin(22), num_lines=4, num_columns=20)

# Husk at LCD er 0-indekseret
lcd.clear() # Metoden clear rydder display for eventuelt tekst der allerede vises
lcd.move_to(0,0) # Metoden move_to flytter markøren til 1. kolonne på linje 1
variabel="Linje 1" # Man kan også benytte variabel og f-string literals
lcd.putstr(f'{variabel}')

lcd.move_to(1,1) # Metoden move_to flytter markøren til 2. kolonne på linje 2
lcd.putstr('Linje 2')

lcd.move_to(2,2) # Metoden move_to flytter markøren til 3. kolonne på linje 3
lcd.putstr('Linje 3')

lcd.move_to(3,3) # Metoden move_to flytter markøren til 4. kolonne på linje 4
lcd.putstr('Linje 4')
# Ryk tilbage til linje 1, kolonne 1
lcd.move_to(0,0)
lcd.blink_cursor_on() # Blink markøren

