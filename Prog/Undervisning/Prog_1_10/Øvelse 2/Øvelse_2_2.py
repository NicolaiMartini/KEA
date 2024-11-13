"""
2.2 - Prøv at vække ESP32 fra deepsleep med en timer,
og kør en funktion der sætter en random farve
på educaboardets neopixels LED4 og LED5
hver gang ESP32 vækkes fra deepsleep.
"""

from machine import Pin, deepsleep
import esp32
from time import sleep
from neopixel import NeoPixel
from random import choice

pushbutton=Pin(0,Pin.IN,Pin.PULL_UP)
n=2
np=NeoPixel(Pin(26,Pin.OUT),n)

def set_color(r,g,b):
    for i in range(n):
        np[i]=(r,g,b)
    np.write()
#     
# def set_color(r,g,b):
#     for i in range(n):
#         np[i]=(r,g,b)
#     np.write()

esp32.wake_on_ext0(pin=pushbutton,level=esp32.WAKEUP_ALL_LOW)
print("I've woken up.")
rand1=randint(0,50)
rand2=randint(0,50)
rand3=randint(0,50)
mylist=[rand1,rand2,rand3]
while True:
    set_color(choice(mylist),choice(mylist),choice(mylist))
    print("I'm going to sleep now.")
    sleep(0.2)
    
#     deepsleep()