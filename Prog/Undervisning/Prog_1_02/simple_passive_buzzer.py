from machine import Pin, PWM
from time import sleep

BUZZER_PIN=14
buzzer_pin=Pin(14,Pin.OUT)
buzzer_pwm=PWM(buzzer_pin,duty=0)

def buzzer(pwm_object,frequency,tone_duration,silence_duration):
    pwm_object.duty(512)
    pwm_object.freq(frequency)
    sleep(tone_duration)
    pwm_object.duty(0)
    sleep(silence_duration)

tones=[262,294,330,349,392,440,494]

while True:
    for list_item in tones:
        buzzer(buzzer_pwm,list_item,0.1,0.1)
        buzzer(buzzer_pwm,list_item,0.1,0.11)

# Se ovenstående
# buzzer(buzzer_pwm,440,0.5,0.2)
# buzzer(buzzer_pwm,294,1.1,0.2)
# buzzer(buzzer_pwm,262,0.8,0.2)
# buzzer(buzzer_pwm,330,0.6,0.2)
# buzzer(buzzer_pwm,349,1.3,0.2)
# buzzer(buzzer_pwm,392,1.8,0.2)
# buzzer(buzzer_pwm,440,1.1,0.2)
# buzzer(buzzer_pwm,494,1.9,0.2)