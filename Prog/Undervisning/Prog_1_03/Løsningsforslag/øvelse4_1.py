"""
4.1 - Sæt individuelle pixel farver så index 0-2 er grønne,
index 3-5 er blå, index 6-8 er røde og index 9-11 er gule
(Forbind gnd til gnd og 5v til 5v og DI til GPIO 26)
"""


# importer NeoPixel klassen fra neopixel modulet
# importer Pin klassen fra machine modulet
# importer sleep funktionen fra time modulet
from machine import Pin
from neopixel import NeoPixel
from time import sleep

# lav en integer variabel med antallet af pixels der skal anvendes
# navngiv variablen NUMBER_OF_PIXELS
NUMBER_OF_PIXELS = 12
p = 26

# lav et neopixel objekt og navngiv det np
np = NeoPixel(Pin(p, Pin.OUT), NUMBER_OF_PIXELS)


# sæt pixels på index 0-2 til at være grønne (r, g, b)
np[0] = (0, 100, 0)
np[1] = (0, 100, 0)
np[2] = (0, 100, 0)
# sæt pixels på index 3-5 til at være blå (r, g, b)
np[3] = (0, 0, 100)
np[4] = (0, 0, 100)
np[5] = (0, 0, 100)
# sæt pixels på index 6-8 til at være røde (r, g, b)
np[6] = (100, 0, 0)
np[7] = (100, 0, 0)
np[8] = (100, 0, 0)
# sæt pixels på index 9-11 til at være gule (r, g, b)
np[9] = (100, 100, 0)
np[10] = (100, 100, 0)
np[11] = (100, 100, 0)

# brug nu NeoPixel objektets write metode til at sende instruktionen
# så skulle de angivne pixels gerne tænde i de angivne farver.
np.write()
    
    
    