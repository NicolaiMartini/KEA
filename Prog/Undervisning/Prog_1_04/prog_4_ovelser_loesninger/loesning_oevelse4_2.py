"""
Del 2 - Lav en funktion der kører et for loop som tænder én pixel
hele vejen rundt i neopixel ringen imens de andre er slukket.
Den skal tage 1 parameter som skal være tiden der skal gå mellem
hver pixel der tændes i ringen. Tiden skal styres ved at dreje på potentiometeret.
"""

# importer NeoPixel klassen fra neopixel modulet
from neopixel import NeoPixel
# importer Pin klassen fra machine modulet
from machine import Pin, ADC
# importer sleep funktionen fra time modulet
from time import sleep_ms

# lav instans af ADC klassen og navngiv den pot
pot = ADC(Pin(34, Pin.IN))
# sætter attenuation til 11dB (150mV - 2450mV)
pot.atten(ADC.ATTN_11DB)

# lav en integer variabel med antallet af pixels der skal anvendes
# navngiv variablen NUMBER_OF_PIXELS
NUMBER_OF_PIXELS = 12 
p = 26 # her laves endnu en integer til valg af GPIO
# lav et neopixel objekt og navngiv det np
np = NeoPixel(Pin(p, Pin.OUT), NUMBER_OF_PIXELS)

# funktion til at rotere en pixel i neopixel ringen
def spin_pixel(speed):
    """ takes one argument speed in milliseconds"""
    for pixel in range(NUMBER_OF_PIXELS):
        np[pixel] = (100, 0, 0)
        np.write()
        # passerer og indsætter argumentet speed i sleep_ms funktionen
        sleep_ms(speed) # tiden pixel vil være tændt 
        np[pixel] = (0, 0, 0) # sluk pixel igen så der kun er én tændt af gangen
        np.write() 
# starter uendelig løkke
while True:
    # kalder spin_pixel funktionen
    # indsætter pot.read() som argument, hvor returværdien vil være mellem 0-4095
    # værdien vil ændres når der skrues på potentiometeret
    # denne værdi passeres ind i sleep_ms funktionskaldet og vil styre hastigheden
    # på den måde vil hver pixel være tændt mellem 0-4095 millisekunder
    spin_pixel(pot.read())
        