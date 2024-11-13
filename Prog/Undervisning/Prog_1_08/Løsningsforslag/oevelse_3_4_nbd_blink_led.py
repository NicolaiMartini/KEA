from machine import TouchPad, Pin
from time import ticks_ms
"""
prog #8 - øvelse 3.4
Prøv at lave en klasse til at blinke LED’er med non-blocking delays med ticks_ms.
Klasen skal tage et Pin objekt som 1. argument og perioden i millisekunder
der skal blinkes med som 2. argument.
"""


# på educaboard kan pin 0, 14, 15 bruges til touch
touch1 = TouchPad(Pin(0, Pin.IN))
touch2 = TouchPad(Pin(15, Pin.IN))
touch3 = TouchPad(Pin(14, Pin.IN))

led1 = Pin(26, Pin.OUT)
# husk at forbind educaboard pins til LED2 og LED3 med dupont kabler
led2 = Pin(12, Pin.OUT) # JP6 GP2 → MISO
led3 = Pin(13, Pin.OUT) # GP3 → MOSI på JP1

class Blink:
    def __init__(self, led, period):
        self.start = ticks_ms()
        self.led = led
        self.period = period
        
    def toggle(self):
        if ticks_ms() - self.start > self.period:
            self.led.value(not self.led.value())
            self.start = ticks_ms()

red = Blink(led1, 500)
yellow = Blink(led2, 800)
green = Blink(led3, 1100)

while True:
    if touch1.read() < 150:
        red.toggle()
        
    if touch2.read() < 150:
        yellow.toggle()
        
    if touch3.read() < 150:
        green.toggle()