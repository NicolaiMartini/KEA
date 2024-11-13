# 4.4 - Lav et program der spiller 4 forskellige toner på buzzeren.
# Hver gang en ny tone spilles skal en ny farve vises på neopixel ringen. (Brug buzzer funktionen)


from machine import Pin, PWM
from neopixel import NeoPixel
from time import sleep, sleep_ms

n = 12 # number of pixels in the Neopixel ring
p = 12 # pin attached to Neopixel ring
np = NeoPixel(Pin(p, Pin.OUT), n) # create NeoPixel instance

A5 = 932 # Tone og frekvens
C5 = 523
C6 = 1046
G5 = 784
GH5 = 831
E5 = 659
F5 = 698
FH5 = 740
CH5 = 554
CH6 = 1109 

def set_color(light):
    np[neopix]=(light[0],light[1],light[2])
    np.write()

buzzer_PWM_objekt = PWM(Pin(14,Pin.OUT),freq=1,duty=0) #freq og duty er de samme som dem der bliver manipuleret i funktionen

tones=[C5,C6,G5,E5]
durations=[80,80,80,80]
lights=[(55,0,0),(0,55,0),(0,0,55),(0,55,55)]
neopixels=[np[3],np[6],np[9],np[11]]

def buzzer(buzzer_PWM_objekt,frequency,tone_duration):
    buzzer_PWM_objekt.duty(512)
    buzzer_PWM_objekt.freq(frequency)
    sleep_time=int(tone_duration*1.3)
    sleep_ms(int(tone_duration*1.3))
    buzzer_PWM_objekt.duty(0)
#     sleep_ms(int(tone_duration*1.3)) # Er funktionen bedre eller værre med afsluttende sleep??

for tone,duration, in zip(tones,durations):
    buzzer(buzzer_PWM_objekt,tone,duration)

for neopix,light in zip(neopixels,lights):
    set_color(light)
    print(light)
#     print(neopix)
    sleep(0.5)