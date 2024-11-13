# Øvelser med funktioner​
from machine import Pin
from time import sleep

Red_LED=Pin(26,Pin.OUT) # LED1 -> GPIO 26​
Yellow_LED=Pin(12,Pin.OUT) # LED2 -> GPIO 12​
Green_LED=Pin(13,Pin.OUT) # # LED3 -> GPIO 13​
Red_LED.off()
Yellow_LED.on()
Green_LED.off()

# husk at forbinde følgende med dupont kabler på Educaboard for at omgå port expander:​
# JP1-MISO og JP6-GP2 for at styre LED2 på GPIO/pin 12 ​
# JP1-MOSI og JP6-GP3 for at styre LED3 på GPIO/pin 13 ​

# 2 lav en funktion der kan tænde LED1, LED2 og LED3 på Educaboardet​

# Funktionen skal ikke tage nogle argumenter​

def all_LEDS_toggle():
    Red_LED.value(not Red_LED.value())
    Yellow_LED.value(not Yellow_LED.value())
    Green_LED.value(not Green_LED.value())
    
# Lav kode til at teste at all_LEDS_on() og all_LEDS_off() virker ved at kalde dem 40 gange​

# - brug et loop og sørg for at LED'erne tændes og slukkes med 50 millisekunders interval​

for i in range(40):
    all_LEDS_toggle()
    sleep(0.05)