from machine import Pin, ADC
from time import sleep
from neopixel import NeoPixel

pot = ADC(Pin(34, Pin.IN))
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_12BIT)

n = 12 # number of pixels in the Neopixel ring
p = 12 # pin atached to Neopixel ring
np = NeoPixel(Pin(p, Pin.OUT), n) # create NeoPixel instance
maxLight = 50 #Max lys
while True:
    #print (pot.read()) #Fejlsøgning
    #print (pot.read()/4095*3.3) #Fejlsøgning
    light = int(pot.read()/4095*maxLight)
    #print (light) #Fejlsøgning
    sleep(0.01)
    for i in range(n):
        np[i] = (light,light,light)
        np.write()