# from machine import Pin
# 
# RED_PIN = 26
# led1 = Pin(RED_PIN, Pin.OUT)
# led1.on()

from machine import Pin
from time import sleep

RED_PIN=26
LED1=Pin(RED_PIN,Pin.OUT)
LED1.on()

while True:
    print("Red LED1 ON!")
    LED1.on()
    sleep(1)
    print("Red LED1 OFF!")
    LED1.off()
    sleep(1)