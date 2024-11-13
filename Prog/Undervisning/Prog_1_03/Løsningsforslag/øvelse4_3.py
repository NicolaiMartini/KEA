"""
4.3 - Find koden fra Micropython grundbogen og prøv
funktionen til at fade farverne i neopixels ringen
(MODULE 6 - Control an Addressable RGB LED Strip)
"""
# importer NeoPixel klassen fra neopixel modulet
from neopixel import NeoPixel
# importer Pin klassen fra machine modulet
from machine import Pin
# importer sleep funktionen fra time modulet
import time
# lav en integer variabel med antallet af pixels der skal anvendes
# navngiv variablen NUMBER_OF_PIXELS
n = 12
p = 26
# lav et neopixel objekt og navngiv det np
np = NeoPixel(Pin(p, Pin.OUT), n)

# fade in/out
def fade_in_out(color, wait):
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
                if color == 'red':
                    np[j] = (val, 0, 0)
                elif color == 'green':
                    np[j] = (0, val, 0)
                elif color == 'blue':
                    np[j] = (0, 0, val)
                elif color == 'purple':
                    np[j] = (val, 0, val)
                elif color == 'yellow':
                    np[j] = (val, val, 0)
                elif color == 'teal':
                    np[j] = (0, val, val)
                elif color == 'white':
                    np[j] = (val, val, val)
            np.write()
        time.sleep_ms(wait)
    
fade_in_out('red', 0)
fade_in_out('green', 10)
fade_in_out('blue', 25)
fade_in_out('purple', 10)
fade_in_out('yellow', 10)
fade_in_out('teal', 10)
fade_in_out('white', 10)