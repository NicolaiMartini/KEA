# Neopixels - Øvelse 4 (Hjemmearbejde): 4.0 - På educaboardet er der 2 neopixels som deler GPIO 26 med LED1.
# Prøv at lave et NeoPixel objekt som er tilkoblet GPIO 26.

from neopixel import NeoPixel
from time import sleep
from machine import Pin
 
n = 3 # number of pixels in the Neopixel ring
p = 12 # pin attached to Neopixel ring
np = NeoPixel(Pin(p, Pin.OUT), n) # create NeoPixel instance
 
np[0] = (0, 255, 0) # set pixel 0 to white (r, g b)
np[1]=(255,0,0)
np[2]=(0,0,255)
np.write() # write to pixels