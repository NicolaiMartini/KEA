from machine import Pin
from time import sleep
from random import uniform, randint
import random

RED_PIN=26
LED1=Pin(RED_PIN,Pin.OUT)

YELLOW_PIN=12
LED2=Pin(YELLOW_PIN, Pin.OUT)

GREEN_PIN=13
LED3=Pin(GREEN_PIN, Pin.OUT)

LED1.off()
LED2.on()
LED3.off()

count=3
while True:
    if count==0:
        break
    else:
        print(f"Countdown until start: {count} seconds")
        count-=1
        sleep(1)
        
while True:
    randomint=randint(1,10)
    sleeptimer=random.uniform(0.1,0.9)
    if 4>randomint>=1:
        LED1.value(not LED1.value())
        print("RED LED1 ON!")
        count+=1
        sleep(sleeptimer)
    elif 7>randomint<=4:
        LED2.value(not LED1.value())
        print("YELLOW LED2 OFF!")
        sleep(sleeptimer)
    elif 10>=randomint<7:
        LED3.value(not LED1.value())
        print("GREEN LED3 ON!")
        sleep(sleeptimer)
