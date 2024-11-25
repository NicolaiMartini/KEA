from machine import Pin
from time import sleep

RED_PIN=26
LED1=Pin(RED_PIN,Pin.OUT)
LED1.off() # Make sure RED is disabled from start

while True:
    LED1.value(not LED1.value()) # Change state to "what it wasn't before"
    sleep(1)