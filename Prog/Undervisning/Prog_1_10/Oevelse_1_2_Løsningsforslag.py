"""
"""

from hcsr04 import HCSR04
from time import ticks_ms
from machine import Pin, PWM

start=ticks_ms()
threshold=100

# Opretter instans af HCSR04 klassen
sensor=HCSR04(15,34)
led1=Pin(26, Pin.OUT)
led1_PWM=PWM(led1)

# Starter event loop
while True:
    # Kalder distance_cm metoden og gemmer returværdien i variablen distance
    if ticks_ms()-start>threshold:
        distance=sensor.distance_cm()*4
        if distance>1023:
            led1_PWM.duty(1023)
        elif distance<1:
            led1_PWM.duty(1)
        else:
            led1_PWM.duty(distance)
        print(f"Distance: {distance} cm")
        start=ticks_ms()

