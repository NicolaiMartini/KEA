from machine import Pin, ADC
from time import sleep
from neopixel import NeoPixel

pot = ADC(Pin(34, Pin.IN))
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_12BIT)

n = 12 # number of pixels in the Neopixel ring
p = 12 # pin atached to Neopixel ring
np = NeoPixel(Pin(p, Pin.OUT), n) # create NeoPixel instance
light = 20
while True:
    #print (pot.read())
    #print (pot.read()/4095*3.3)
    i = int(pot.read()/4095*47)
    #print (i)
    sleep(0.0001)
    if i > 11:
        if i <= 23:
            i -= 12
        if i >= 24 and i <= 35:
            i -= 12*2
        if i >= 36:
            i -= 12*3
    for x in range(n):
        if x == i:
            np[x] = (light,light,light)
            np.write()
        else:
            np[x] = (0,0,0)
            np.write()
