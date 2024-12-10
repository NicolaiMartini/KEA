from neopixel import NeoPixel
from machine import Pin
from time import sleep_ms

#ANVENDER IKKE POT-METERET!

n = 12 # number of pixels in the Neopixel ring
p = 12 # pin atached to Neopixel ring
np = NeoPixel(Pin(p, Pin.OUT), n) # create NeoPixel instance
maxLight = 150 #Maximal lysstyrke
sleepMS = 5  #Hastigheden lyset skal ændre sig i

def clear(): #ClearFunktion til NeoPixel-ringen
    for i in range(n):
        np[i] = (0, 0, 0)
        np.write()

for y in range(5):        #Hvor mange gange skal fade-loopet køre
    for x in range(maxLight): #Skruer op for lyset
        for z in range(n):    #Konfigurerer alle pixels indenfor n
            np[z] = (x,x,x)   #Alle pixels bliver opdateret med den nye farve
            np.write()
        sleep_ms(sleepMS) #Bestemmer hastigheden i ms som lyset ændrer sig
        print(x)
    for x in range(maxLight):  #Skruer ned for lyset
        for z in range(n):     #Konfigurerer alle pixels indenfor n
            xx = maxLight - x  #Trækker x fra, så vi skruer ned, fremfor op
            np[z] = (xx,xx,xx) #Alle pixels bliver opdateret med den nye farve
            np.write()
        sleep_ms(sleepMS) #Bestemmer hastigheden i ms som lyset ændrer sig
        print(xx)
print("Slukker lys")
clear()

