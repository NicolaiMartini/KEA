from machine import Pin
from time import sleep

RED_PIN=26
LED1=Pin(RED_PIN,Pin.OUT)
LED1.off()

YELLOW_PIN=12
LED2=Pin(YELLOW_PIN, Pin.OUT)
LED2.on()

GREEN_PIN=13
LED3=Pin(GREEN_PIN, Pin.OUT)
LED3.off()

while True:
    #Red on
    LED1.value(not LED1.value())
    sleep(2)
    
    # Yellow on
    LED2.value(not LED2.value())
    sleep(1)
    
    # Red off, Yellow off, Green on
    LED1.value(not LED1.value())
    LED2.value(not LED2.value())
    LED3.value(not LED3.value())
    sleep(2)
    
    # Yellow on, Green off
    LED3.value(not LED3.value())
    LED2.value(not LED2.value())
    sleep(1)
    # Yellow off
    LED2.value(not LED2.value())
