"""
Øvelse 4.2

Brug set_color() funktionen til at sætte alle neopixels til 
og brug derefter clear() funktionen til at slukke dem. 
Kør begge funktioner i en while løkke med et 
interval på 1 sekund mellem dem så der blinkes i rød 10 gange. ​

Sørg for at afprøve koden på den fysiske hardware!
Lav en fil kaldet oevelse_4_2.py i Thonny og kopier koden ind der.

Skriv koden der mangler under hver kommentar:
"""


# importer NeoPixel klassen fra neopixel modulet
from neopixel import NeoPixel
# importer Pin klassen fra machine modulet
from machine import Pin
# importer sleep funktionen fra time modulet
from time import sleep
# lav en integer variabel med antallet af pixels der skal anvendes
# navngiv variablen NUMBER_OF_PIXELS
NUMBER_OF_PIXELS = 12
p = 26
# lav et neopixel objekt og navngiv det np
np = NeoPixel(Pin(p, Pin.OUT), NUMBER_OF_PIXELS)
# færdiggør funktionen set_color()
def set_color(r, g, b):
    for pixel in range(NUMBER_OF_PIXELS):
        np[pixel] = (r, g, b)
    np.write()
        

# færdiggør funktionen clear()
def clear():
    for pixel in range(NUMBER_OF_PIXELS):
        np[pixel] = (0, 0, 0)
    np.write()            
    
    

# start et for loop der gentager en handling 10 gange
for i in range(10):
    # kald funktionen set_color() for at tænde alle pixels i rød
    set_color(100, 0, 0)
    # sæt tid pixels skal være tændt med sleep funktionen
    sleep(1)
    # kald funktionen clear() for at slukke alle pixels
    clear()
    # sæt tid pixels skal være slukkede med sleep funktionen
    sleep(1)