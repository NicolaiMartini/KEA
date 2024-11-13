"""
2.1 - Vælg en digital input sensor
(Fx, trykknap eller PIR)
og anvend den til at vække ESP32 fra deepsleep
og print en besked om at ESP32 er vågnet i shell
og toggle en LED1 10 gange.
(husk at filen skal ligge på ESP32 som main.py)
- brug wake_on_ext0:
https://docs.micropython.org/en/latest/library/esp32.html#esp32.wake_on_ext0
"""

from machine import Pin, deepsleep
from time import sleep
import esp32

led_pin=26
led1=Pin(led_pin,Pin.OUT)
pushbutton=Pin(0,Pin.IN,Pin.PULL_UP)

esp32.wake_on_ext0(pin=pushbutton,level=esp32.WAKEUP_ALL_LOW)
print("I've woken up.")


while True:
    for i in range(1,6):
        print(i)
        sleep(0.5)
    for i in range(1,11):
        led1.value(not led1.value())
        sleep(0.2)
        print(i)
    print("I'm going to sleep now.")
    sleep(2)
    deepsleep()