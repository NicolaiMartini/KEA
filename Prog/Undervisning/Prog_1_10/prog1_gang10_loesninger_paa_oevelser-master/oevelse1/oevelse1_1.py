from hcsr04 import HCSR04
from machine import Pin
from time import ticks_ms, sleep_ms
"""
1.1 - upload modulet til at arbejde med ultralydsmodulet til ESP32 og læg den I mappen lib. ​
https://randomnerdtutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266/ ​

Lav et uendeligt loop med et non-blocking delay der printer distancen i CM
der måles af HC-SR04 ultralydssensoren hvert 100 millisekund.
(Se eksemplerne fra artiklen,og e bort fra afsnittet med Oled displayet).
Brug trigger_pin=15, echo_pin=34, og bemærk at
GPIO 34 deler kredsløb med potmeter på educaboard og
potmeter skal ikke være drejet helt til højre eller venstre ellers får man ugyldige målinger!)​

"""
usonic = HCSR04(trigger_pin=15, echo_pin=34, echo_timeout_us=10000)

start = ticks_ms()
delay_ms = 300

while True:
    if ticks_ms() - start > delay_ms:
        print(usonic.distance_cm())
        start = ticks_ms()
    sleep_ms(10)