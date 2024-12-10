"""
4.4 - Lav et program der spiller 4 forskellige toner på buzzeren.
Hver gang en ny tone spilles skal en ny farve vises på neopixel ringen.
(Brug buzzer funktionen fra sidste uges undervisning)​
"""
from machine import Pin, PWM
from time import sleep_ms
from neopixel import NeoPixel
# antal pixels
NUMBER_OF_PIXELS = 12
# GPIO Pin nummer
p = 12

# lav et neopixel objekt og navngiv det np
np = NeoPixel(Pin(p, Pin.OUT), NUMBER_OF_PIXELS)
# lav PWM objekt til buzzer
buzz_obj = PWM(Pin(14, Pin.OUT), duty=0)
# lav liste med tuples til farver
colors = [(20, 0, 20), (20, 20, 0), (0, 20, 20), (20, 10, 0)]
# lav liste med toner
tones = [440, 494, 523, 583]
# har sat argument så funktione tager en hel tuple som argument
def set_color(color_tuple): 
    for pixel in range(NUMBER_OF_PIXELS):
        np[pixel] = color_tuple
    np.write()
        
def buzz(pwm_obj, tone_hz, tone_duration, pause_duration):
    pwm_obj.duty(512)
    pwm_obj.freq(tone_hz)
    sleep_ms(tone_duration)
    pwm_obj.duty(0)
    sleep_ms(pause_duration)
# for loop hvor der loopes 4 gange
# i får værdier fra 0 til 3
for i in range(4):
    # sæt farven fra liste med tuples på index i
    set_color(colors[i])
    # sæt tonen fra liste toner på index i
    buzz(buzz_obj, tones[i], 200, 100)

set_color((0, 0, 0)) # slukker neopixel ringen igen