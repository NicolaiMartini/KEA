from machine import Pin
from time import sleep

led_pin=22
LED=Pin(led_pin,Pin.OUT)

while True:
    LED.value(not LED.value())
    sleep(2)