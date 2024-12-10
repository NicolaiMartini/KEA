"""1.2 - prøv at styre lysintensitet med PWM på LED1, så lysintensitet øges jo længere væk noget er fra educaboard."""

from hcsr04 import HCSR04
from machine import Pin, PWM
from neopixel import NeoPixel
from time import sleep

# Opretter instans af HCSR04 klassen
sensor=HCSR04(15,34)
led=Pin(26,Pin.OUT)
n=2
np=NeoPixel(Pin(26,Pin.OUT),n)

def set_color(r,g,b):
    for i in range(n):
        np[i]=(r,g,b)
    np.write()


# Starter event loop
while True:
	# Kalder distance_cm metoden og gemmer returværdien i variablen distance
	distance=sensor.distance_cm()
	print(f"Distance: {distance} cm")
	set_color(0,0,0)
	sleep(0.1)