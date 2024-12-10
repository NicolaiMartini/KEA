from machine import Pin
from time import sleep
pinin=Pin(22, Pin.IN)
pinout=Pin(14, Pin.OUT)

while True:
    pinout.value(not pinin.value())
    print(pinout.value())
    sleep(0.1)
#     pinout.value(not pinin.value())
#     print(pinout.value())
#     sleep(1)