from machine import Pin
from time import sleep

PB1 = Pin(4, Pin.IN)
LED1 = Pin(26, Pin.OUT)

while True:
    print("Knap værdi: ", PB1.value())
    first=PB1.value()
    sleep(0.01)
    second=PB1.value()
