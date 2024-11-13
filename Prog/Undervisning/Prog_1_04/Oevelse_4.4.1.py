from machine import Pin, ADC
from time import sleep_ms, sleep
from neopixel import NeoPixel

# Initialiseret ADC Objekt på Pin 34
pot=ADC(Pin(34,Pin.IN),atten=3)
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_12BIT)
led1=Pin(26,Pin.OUT,value=0)

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

while True:
    pot_val=pot.read()
    spaending=pot_val*(3.3/4096)
    print("\nAnalog potentiometer vaerdi: ", pot_val)
    print("\nAnalog potentiometer spaending: ",spaending)
    led1.value(not led1.value())
    sleep_ms(100)
# Del 1 - Blink alle pixels på neopixel ringen rød når ADC værdien er under 500, og gul når den er over 1500 og grøn når den er over 3000
    if pot_val < 500: # Rød når værdien er under 1500
        for i in range(n):
            set_color(100,0,0) # Rød
    if 500<pot_val<3000: # Gul når værdien er mellem 1500 og 3000
        for i in range(n):
            set_color(100,50,00) # Gul
    if pot_val>3000: # Grøn når værdien er over 3000
        for i in range(n):
            set_color(0,100,0) # Grøn