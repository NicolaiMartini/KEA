from machine import Pin 
from time import sleep 

RED_LED_PIN = 26 
red = Pin(RED_LED_PIN, Pin.OUT) 

YELLOW_LED_PIN = 12 
yellow = Pin(YELLOW_LED_PIN, Pin.OUT) 

GREEN_LED_PIN = 13 
green = Pin(GREEN_LED_PIN, Pin.OUT) 

while True: 
    green.on() 
    sleep(30)
    green.off() 
    yellow.off() # ON
    sleep(2) 
    yellow.on() # OFF
    red.on() 
    sleep(30) 
    yellow.off() # ON 
    sleep(2) 
    yellow.on() # OFF
    red.off() 
    