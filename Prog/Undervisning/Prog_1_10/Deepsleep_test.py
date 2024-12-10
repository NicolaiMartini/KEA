from machine import deepsleep, Pin
from time import sleep

led=Pin(2,Pin.OUT)

# Blink LED
led.value(1)
sleep(1)
led.value(0)
sleep(1)

# Wait 5 seconds so that you can catch the ESP awake to establish a serial communication later
# You should remove this sleep line in your final script
sleep(5)

print("I'm awake, but I'm going to sleep")

# Sleep for 10 seconds (10000 milliseconds)
deepsleep(10000)