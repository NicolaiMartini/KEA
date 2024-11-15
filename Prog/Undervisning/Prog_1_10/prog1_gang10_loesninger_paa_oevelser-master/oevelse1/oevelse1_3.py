from hcsr04 import HCSR04
from machine import Pin, PWM
from time import ticks_ms, sleep_ms

buzz = PWM(Pin(14, Pin.OUT))

"""
1.3 - lav et non-blocking eventloop (uendeligt while loop)der måler distancen fra ultralydmodulet.
Hvis distancen er mellem 10 CM og 20 CM skal buzzeren spille en tone på 220Hz og hvis distancen
er under 10 CM skal buzzeren afspille en tone på 880Hz. Hvis distancen er over 20 CM eller under
0 CM skal buzzeren slukkes. (Husk at forbinde JP6 GP6 – JP1 SCK så kan buzzer anvendes på GPIO 14)​

"""
usonic = HCSR04(trigger_pin=15, echo_pin=34, echo_timeout_us=10000)

start = ticks_ms()
delay_ms = 50

while True:
    if ticks_ms() - start > delay_ms:
        distance = usonic.distance_cm()
        
        print(distance)
        
        if distance > 10 and distance < 20:
            buzz.duty(512)
            buzz.freq(220)

        if distance < 10:
            buzz.duty(512)
            buzz.freq(880)

        if distance < 0 or distance > 120:
            buzz.duty(0)
            
        start = ticks_ms()
    sleep_ms(10)