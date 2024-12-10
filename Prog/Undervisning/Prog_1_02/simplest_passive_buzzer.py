from machine import Pin, PWM
from time import sleep

buzzer=PWM(Pin(14,Pin.OUT),duty=0)

buzzer.duty(512)
buzzer.freq(440) # A4 note
sleep(1)
buzzer.duty(0)
sleep(0.1)
buzzer.duty(512)
buzzer.freq(1319) # E6 note
sleep(1)
buzzer.duty(0)