from machine import Pin
from time import sleep
from random import randint

LED1=Pin(26,Pin.OUT)
LED1.off()

LED2=Pin(12, Pin.OUT)
LED2.on()

LED3=Pin(13, Pin.OUT)
LED3.off()

count=2
while True:
    if count>0:
        print(f"Countdown until start: {count} seconds")
        count-=1
        sleep(1)
    else:
        random=randint(1,3)
        if random==1:
            LED1.value(not LED1.value())
            sleep(0.05)
        elif random==2:
            LED2.value(not LED2.value())
            sleep(0.05)
        else:
            LED3.value(not LED3.value())
            sleep(0.05)
