# 4.1 - Sæt individuelle pixel farver så index 0-2 er grønne, index 3-5 er blå, index 6-8 er røde og index 9-11 er gule (Forbind gnd til gnd og 5v til 5v og DI til GPIO 26)https://wokwi.com/projects/408806446792403969

from neopixel import NeoPixel
from time import sleep
from machine import Pin

n = 12 # number of pixels in the Neopixel ring
p = 12 # pin attached to Neopixel ring
np = NeoPixel(Pin(p, Pin.OUT), n) # create NeoPixel instance

np[0]=(0,50,0) # Grøn
np[1]=(0,50,0)
np[2]=(0,50,0)

np[3]=(0,0,50) # Blå
np[4]=(0,0,50)
np[5]=(0,0,50)

np[6]=(50,0,0) # Rød
np[7]=(50,0,0)
np[8]=(50,0,0)

np[9]=(75,50,0) # Gul
np[10]=(75,50,0)
np[11]=(75,50,0)
np.write()