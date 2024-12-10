from machine import Pin
from time import sleep

led=Pin(12,Pin.OUT)
led2=Pin(14,Pin.OUT)

while True:
    led.value(not led.value())
    led2.value(not led2.value())
    sleep(0.5)