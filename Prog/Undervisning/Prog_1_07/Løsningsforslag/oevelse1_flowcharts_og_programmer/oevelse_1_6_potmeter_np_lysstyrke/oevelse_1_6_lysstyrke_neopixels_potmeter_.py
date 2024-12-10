from machine import Pin, ADC
from time import sleep
from neopixel import NeoPixel

pot = ADC(Pin(34, Pin.IN), atten = 3)

n = 2
np = NeoPixel(Pin(26, Pin.OUT), n)

def set_brigthness(intensity):
    for pixel in range(n):
        np[pixel] = (intensity, intensity, intensity)
        np.write()

old_ADC_reading = 0

while True:
    new_ADC_reading = int(pot.read()/16)
    if new_ADC_reading != old_ADC_reading:
        set_brigthness(new_ADC_reading)
        old_ADC_reading = new_ADC_reading