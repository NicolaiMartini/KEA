from machine import Pin, deepsleep
from time import sleep

sleep_time_ms=4000
# Denne fil skallægge på ESP32som main.py
print("ESP32 woke from deepsleep")
led1=Pin(26,Pin.OUT)
led1.value(1)
sleep(2)
led1.value(0)

print(f"Going to sleep for {sleep_time_ms/1000} seconds")
deepsleep(sleep_time_ms)