from machine import Pin
from time import sleep

pb1 = Pin(4, Pin.IN)
led1 = Pin(26, Pin.OUT)
counter = 0
led2 = Pin(12, Pin.OUT)
led2.on()
already_printed = False

while True:
    if not pb1.value():
        if not already_printed:
            print("Knap værdi:",pb1.value())
            already_printed = True
    if pb1.value() and already_printed:
        counter += 1
        led1.value(not led1.value())
        print("Knap værdi:",pb1.value())
        print("Har trykket knap",counter,"gange.")
        already_printed = False