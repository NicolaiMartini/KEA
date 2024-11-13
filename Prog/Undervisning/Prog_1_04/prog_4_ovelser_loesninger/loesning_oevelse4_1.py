# Prog
"""
Neopixels med ADC og potentiometer - Øvelse 4:​

Del 1 - Blink alle pixels på neopixel ringen rød når ADC
værdien er under 500, og gul når den er over 1500 og grøn
når den er over 3000
"""

# importer NeoPixel klassen fra neopixel modulet
from neopixel import NeoPixel
# importer Pin klassen fra machine modulet
from machine import Pin, ADC
# importer sleep funktionen fra time modulet
from time import sleep_ms

pot = ADC(Pin(34, Pin.IN))
pot.atten(ADC.ATTN_11DB)

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

while True:
    # aflæs potentiometer ADC værdi og tildel værdi til variablen
    adc_value = pot.read() 
    # hvis adc_value er under 500
    if adc_value < 500:
        # sæt pixels i rød farve med set_color() funktionen
        set_color(200, 0, 0)
    # ellers hvis adc_value er over 1500 og under 3000
    elif adc_value > 1500 and adc_value < 3000:
        # sæt pixels i gul farve med set_color() funktionen
        set_color(200, 200, 0)
    # ellers hvis adc_value er over 3000
    elif adc_value > 3000:
        set_color(0, 200, 0)
    # else blok køres når ingen af de forgående betingelser opfyldes
    # dette gælder når adc_value er mellem 500 til 1500
    else:
        # slukkes alle pixels 
        set_color(0, 0, 0)
    # logik der sørger for at pixels blinker    
    sleep_ms(200) # holder pixels tændt i 200 ms i den farve der blev valgt
    set_color(0, 0, 0) # slukker alle pixels
    sleep_ms(200) # holder alle pixels slukket i 200 ms
        