# Øvelser med funktioner
# Husk at importere moduler der skal bruges her, fx, sleep, Pin osv.
from machine import Pin
from time import sleep
# LED1 -> GPIO 26
# LED2 -> GPIO 12
# LED3 -> GPIO 13

# lav et objekt til hver LED
# husk at forbinde følgende med dupont kabler på Educaboard for at omgå port expander:
# JP1-MISO og JP6-GP2 for at styre LED2 på GPIO/pin 12 
# JP1-MOSI og JP6-GP3 for at styre LED3 på GPIO/pin 13 
led1 = Pin(26, Pin.OUT)
led2 = Pin(12, Pin.OUT)
led3 = Pin(13, Pin.OUT)

# 1 lav en funktion der tænder LED 1 på Educaboard hvis den er slukket og som slukker LED 1 hvis den er tændt
# Funktionen skal ikke tage nogle argumenter
def toggle_LED1():
    led1.value(not led1.value())

# Lav kode til at teste at toggle_LED1() funktionen virker ved at kalde den 10 gange
# sørg for at der er 100 millisekunders pause mellem hver gang der tændes og slukkes
# Hint: brug et loop
# - Tjek at LED1 tænder og slukker

for i in range(10):
    toggle_LED1()
    sleep(0.1)

# 2 lav en funktion der kan tænde LED1, LED2 og LED3 på Educaboardet
# Funktionen skal ikke tage nogle argumenter
def all_LEDS_on():
    led1.on()
    led2.off()
    led3.on()

# 2.2 lav en funktion der kan slukke LED1, LED2 og LED3 på Educaboardet
# Funktionen skal ikke tage nogle argumenter
def all_LEDS_off():
    led1.off()
    led2.on()
    led3.off()
    
# Lav kode til at teste at all_LEDS_on() og all_LEDS_off() virker ved at kalde dem 40 gange
# - brug et loop og sørg for at LED'erne tændes og slukkes med 50 millisekunders interval

for i in range(40):
    all_LEDS_on()
    sleep(0.05)
    all_LEDS_off()
    sleep(0.05)

# 3 lav en funktion der tager en liste med integers som argument og returnerer en ny liste hvor hvert
# tal i listen er blevet fordoblet
binary_values_list = [1, 2, 4, 8, 16, 32]

def double_list_values(int_list):
    doubled_list = [] # opretter tom liste til de fordoblede værdier
    for index in int_list: # for loop der gennemløber listen med integers
        doubled_list.append(index+index) # tilføj den forboblede værdi til den nye liste
        
    return doubled_list # returner listen med de fordoblede værdier

print(double_list_values(binary_values_list)) # test at funktionen virker

# 4 lav en funktion der tager en liste med integers som argument og omdanner hvert element til
# en string - Hint brug: str()
def convert_list_values_to_str(int_list):
    str_list = [] # opret en tom liste til string værdierne
    for index in int_list:  # for loop der gennemløber listen med integers
        # Omdan hvert hvert element til string og tilføj til ny liste
        str_list.append(str(index)) 
        
    return str_list # returner listen med string værdierne

print(convert_list_values_to_str(binary_values_list)) # test at funktionen virker
# print output skal vise: ['1', '2', '4', '8', '16', '32']