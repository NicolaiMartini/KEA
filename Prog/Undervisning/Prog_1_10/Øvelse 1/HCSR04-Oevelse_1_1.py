"""Lav et uendeligt loop med et non-blocking delay der printer distancen i CM der måles af HC-SR04 ultralydssensoren hvert 100 millisekund.
(Se eksemplerne fra artiklen,og e bort fra afsnittet med Oled displayet).
Brug trigger_pin=15, echo_pin=34, og bemærk at GPIO 34 deler kredsløb med potmeter på educaboard.
Potmeter skal ikke være drejet helt til højre eller venstre ellers får man ugyldige målinger!)
"""

from hcsr04 import HCSR04
from time import ticks_ms

start=ticks_ms()
threshold=100

# Opretter instans af HCSR04 klassen
sensor=HCSR04(15,34)

# Starter event loop
while True:
	# Kalder distance_cm metoden og gemmer returværdien i variablen distance
	if ticks_ms()-start>threshold:
        distance=sensor.distance_cm()
        print(f"Distance: {distance} cm")
        sleep(0.1)
        start=ticks_ms()
