from machine import Pin, deepsleep
from time import sleep
import esp32

"""
2.1 - Vælg en digital input sensor (Fx, trykknap eller PIR) og
anvend den til at vække ESP32 fra deepsleep og print en besked
om at ESP32 er vågnet i shell og toggle en LED1 10 gange.
(husk at filen skal ligge på ESP32 som main.py) -
brug wake_on_ext0: https://docs.micropython.org/en/latest/library/esp32.html#esp32.wake_on_ext0 
"""
# Denne fil skal overføres til ESP32 og filen skal navngives
# main.py for at virke
print("ESP32 er vågnet")

led1 = Pin(26, Pin.OUT)
for i in range(10):
    led1.value(not led1.value())
    sleep(.05)
# Pull up sørger for at Pin er høj til at starte med
wake_pin = Pin(0, Pin.IN, Pin.PULL_UP)
sleep(4)
esp32.wake_on_ext0(pin = wake_pin,
                   level = esp32.WAKEUP_ALL_LOW)
print("ESP32 går i deepsleep og kan vækkes med PB2")
deepsleep()