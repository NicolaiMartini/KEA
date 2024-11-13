# External Wake up - ext0
import esp32
from machine import Pin
from machine import deepsleep
from time import sleep

wake1=Pin(14,mode=Pin.IN)

# Level parameter can be: esp32.WAKEUP_ANY_HIGH or esp32.WAKEUP_ALL_LOW
esp32.wake_on_ext0(pin=wake1,level=esp32.WAKEUP_ANY_HIGH)

# Your main code goes here to perform a task

print("I'm awake. Going to sleep in 10 seconds.")
sleep(10)
print("I'm going to sleep now.")
deepsleep()