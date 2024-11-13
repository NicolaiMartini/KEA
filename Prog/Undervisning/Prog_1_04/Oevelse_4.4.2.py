from machine import Pin, ADC
from time import sleep, sleep_ms
from neopixel import NeoPixel

# Initialiseret ADC Objekt på Pin 34
pot=ADC(Pin(34,Pin.IN),atten=3)
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_12BIT)
led1=Pin(26,Pin.OUT,value=0)

n = 12 # number of pixels in the Neopixel ring
p = 12 # pin attached to Neopixel ring
np = NeoPixel(Pin(p, Pin.OUT), n) # create NeoPixel instance

def pot_np(pot_input): # Definer den funktion som skal benyttes
    for i in range(n): # Få en relativ OK-værdi til 
        np[i]=(100,50,20) # Den farve der skal vises i LED
        np.write() # Aktiver Få LED'en til at lyse
        sleep(0.1) # Hvor længe LED'en lyser
        np[i]=(0,0,0) # "Den farve" - (0,0,0) er slukket.
        np.write() # "Tænd" det slukkede lys
        sleep(pot.read()/1500) # Hvor lang tid der går mellem hver LED

# pot_np(pot.read()) # Nu kører funktionen én gang.

while True:
    pot_np(pot.read())
# Indsæt i while True-løkke for at få den til at fortsætte.