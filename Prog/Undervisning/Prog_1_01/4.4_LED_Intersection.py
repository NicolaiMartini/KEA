from machine import Pin
from time import sleep

RED_PIN=26
LED1=Pin(RED_PIN,Pin.OUT)
LED1.off() # Disable Red LED from start

YELLOW_PIN=12
LED2=Pin(YELLOW_PIN, Pin.OUT)
LED2.on() # Disable Yellow LED from start

GREEN_PIN=13
LED3=Pin(GREEN_PIN, Pin.OUT)
LED3.off() # Disable Green LED from start

while True:
    LED1.value(not LED1.value()) # Change state to "the other one".
    LED2.value(not LED2.value()) # -||-
    LED3.value(not LED3.value()) # -||-
    sleep(1)
