# 4.2 - Brug set_color() funktionen til at sætte alle neopixels til rød og brug derefter clear() funktionen til at slukke dem.
# Kør begge funktioner i en while løkke med et interval på 1 sekund mellem dem så der blinkes i rød 10 gange. https://wokwi.com/projects/408810200328666113

from neopixel import NeoPixel
from time import sleep
from machine import Pin

n = 12 # number of pixels in the Neopixel ring
p = 12 # pin attached to Neopixel ring
np = NeoPixel(Pin(p, Pin.OUT), n) # create NeoPixel instance

def clear():
    for i in range(n):
        np[i]=(0,0,0)
        np.write()
        sleep(0.2)

def set_color(r,g,b):
    for i in range(n):
        np[i]=(r,g,b)
    np.write()
    
for i in range(10):
    set_color(255,0,0)
    sleep(0.5)
    clear()
    sleep(0.5)