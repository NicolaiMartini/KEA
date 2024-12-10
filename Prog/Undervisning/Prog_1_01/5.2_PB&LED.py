from machine import Pin
from time import sleep

PB1 = Pin(4, Pin.IN)
LED1 = Pin(26, Pin.OUT)

while True:
    first=PB1.value()
    sleep(0.01)
    second=PB1.value()
    if first==1 and second==0:
        print("The button is pressed.") # Can be left out
        LED1.value(not LED1.value())
    if first==0 and second ==1: # Can be left out
        print("The busson is released.") # Can be left out
