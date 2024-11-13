from machine import Pin, PWM
from time import sleep_ms

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

buzzer_PWM_objekt = PWM(Pin(14,Pin.OUT),freq=1,duty=0) #freq og duty er de samme som dem der bliver manipuleret i funktionen

tones=[C5,C6,G5,E5,C6,G5,E5,CH5,CH6,GH5,F5,CH6,GH5,F5,C5,C6,G5,E5,C6,G5,E5,G5,F5,GH5,A5,GH5,A5,C6,C6]
durations=[80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,40,80,40,140,140]
def buzzer(buzzer_PWM_objekt,frequency,tone_duration):
    buzzer_PWM_objekt.duty(512)
    buzzer_PWM_objekt.freq(frequency)
    sleep_time=int(tone_duration*1.3)
    sleep_ms(int(tone_duration*1.3))
    buzzer_PWM_objekt.duty(0)
#     sleep_ms(int(tone_duration*1.3)) # Er funktionen bedre eller værre med afsluttende sleep??

for tone,duration in zip(tones,durations):
    buzzer(buzzer_PWM_objekt,tone,duration)

# Dict over toner + tonelængde
# tones={C5:80,C6:80,G5:80,E5:80,C6:80,G5:80,E5:80,CH5:80,CH6:80,GH5:80,F5:80,CH6:80,
#        GH5:80,F5:80,C5:80,C6:80,G5:80,E5:80,C6:80,G5:80,E5:80,G5:80,F5:80,GH5:80,
#        A5:40,GH5:80,A5:40,C6:140,C6:140}
# Men hov, Dicts virker ikke til det her - FOR DICTS TILLADDER IKKE DUPLICATES.
