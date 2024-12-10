from machine import Pin
from time import sleep

LED_PIN=14
LED=Pin(LED_PIN,Pin.OUT)

while True:
    LED.off()
    sleep(5)
    LED.on()
    sleep(2)