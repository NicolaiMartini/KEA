from machine import Pin
from time import sleep

RED_PIN=26 # Connect RED LED to PIN26
LED1=Pin(RED_PIN,Pin.OUT) # Instantiate LED1
LED1.off() # Disable RED LED by default

YELLOW_PIN=12 # Connect YELLOW LED to PIN12
LED2=Pin(YELLOW_PIN, Pin.OUT) # Instantiate LED2
LED2.on() # Disable YELLOW LED by default

GREEN_PIN=13 # Connect GREEN LED to PIN13
LED3=Pin(GREEN_PIN, Pin.OUT) # Instantiate LED3
LED3.off() # Disable GREEN LED by default

while True:
    LED1.value(not LED1.value()) # Change LED state
    print("RED LED1 ON!") # Can be deleted
    sleep(0.5)
    LED2.value(not LED2.value()) # Change LED state
    print("YELLOW LED2 OFF!") # Can be deleted
    sleep(0.5)
    LED3.value(not LED3.value()) # Change LED state
    print("GREEN LED3 ON!") # Can be deleted
    sleep(0.5)