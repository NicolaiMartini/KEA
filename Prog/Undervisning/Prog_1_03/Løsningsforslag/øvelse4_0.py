"""
4.0 - På educaboardet er der 2 neopixels som deler GPIO 26 med LED1.
Prøv at lave et NeoPixel objekt som er tilkoblet GPIO 26.
Lav et program hvor at pixel index 0 lyser grønt I 0.3 sekund og derefter slukker.
Få derefter pixel på index 1 til at lyse I farven blå I 0.3 sekund og sluk den derefter.
Brug et loop til at sørge for at de skiftevis tænder og slukker for evigt.
"""
from machine import Pin
from neopixel import NeoPixel
from time import sleep

n = 2
p = 26

np = NeoPixel(Pin(p, Pin.OUT), n)

while 1:
    np[0] = (0, 100, 0)
    np.write()
    sleep(0.3)
    np[0] = (0, 0, 0)
    np[1] = (0, 0, 100)
    np.write()
    sleep(0.3)
    np[1] = (0, 0, 0)
    np.write()
    
    
    