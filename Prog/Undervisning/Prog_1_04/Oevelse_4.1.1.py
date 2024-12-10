# Øvelser med funktioner​
from machine import Pin
from time import sleep

Red_LED=Pin(26,Pin.OUT) # LED1 -> GPIO 26​
Yellow_LED=Pin(12,Pin.OUT) # LED2 -> GPIO 12​
Green_LED=Pin(13,Pin.OUT) # # LED3 -> GPIO 13​

# husk at forbinde følgende med dupont kabler på Educaboard for at omgå port expander:​
# JP1-MISO og JP6-GP2 for at styre LED2 på GPIO/pin 12 ​
# JP1-MOSI og JP6-GP3 for at styre LED3 på GPIO/pin 13 ​


# 1 lav en funktion der tænder LED 1 på Educaboard hvis den er slukket og som slukker LED 1 hvis den er tændt​

# Funktionen skal ikke tage nogle argumenter​

def toggle_LED1():
    Red_LED.value(not Red_LED.value())

# Lav kode til at teste at toggle_LED1() funktionen virker ved at kalde den 10 gange​
# sørg for at der er 100 millisekunders pause mellem hver gang der tændes og slukkes​
# Hint: brug et loop​
# - Tjek at LED1 tænder og slukker​
for i in range(10): # For hver integer i range(10) skal knappen toggles, altså tænde eller slukke
    toggle_LED1()
    sleep(0.1)
