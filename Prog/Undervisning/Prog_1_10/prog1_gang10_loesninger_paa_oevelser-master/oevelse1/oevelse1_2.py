from hcsr04 import HCSR04
from machine import Pin, PWM
from time import ticks_ms, sleep_ms

led1 = PWM(Pin(26, Pin.OUT))

"""
1.2 - prøv at styre lysintensitet med PWM på LED1, så lysintensitet øges
jo længere væk noget er fra educaboard.

"""
usonic = HCSR04(trigger_pin=15, echo_pin=34, echo_timeout_us=10000)

start = ticks_ms()
delay_ms = 50

while True:
    if ticks_ms() - start > delay_ms:
        distance = usonic.distance_cm()
        print(distance)
        if distance > 0 and distance < 100:
            led1.duty(int(distance * 10))

        start = ticks_ms()
    sleep_ms(10)
