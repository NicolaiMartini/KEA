from machine import Pin, deepsleep
from random import choice
from neopixel import NeoPixel
from time import sleep
"""
2.2 - Prøv at vække ESP32 fra deepsleep med en timer,
og kør en funktion der sætter en random farve på
educaboardets neopixels LED4 og LED5 hver gang ESP32 vækkes fra deepsleep.
"""

PIXEL_AMOUNT = 2
PIXEL_GPIO = 26
np = NeoPixel(Pin(PIXEL_GPIO, Pin.OUT), PIXEL_AMOUNT)
# list with tuples with RGB colors 
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
# use choice funktion to take random tuple from the list 
np[0] = choice(colors) 
np[1] = choice(colors)
np.write()
# sleep is inserted to give time to stop the program between deepsleep
sleep(1) 
# goint to deepsleep for 1000 miliseconds
deepsleep(1000)