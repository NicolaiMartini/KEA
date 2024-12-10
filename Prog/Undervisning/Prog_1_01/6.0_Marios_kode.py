from machine import Pin
from time import sleep

pb1 = Pin(4,Pin.IN)
led1 = Pin(26, Pin.OUT)
led2 = Pin(12, Pin.OUT)
led2.on()
counter=0
while True:
    first = pb1.value()
    sleep(0.01)
    second = pb1.value()
    if first == 1 and second == 0:
        print("Knappen er trykket.",counter)
        counter+=1
        led1.value(not led1.value())
#     elif first == 0 and second == 1:
#         print("Knappen er sluppet.") 