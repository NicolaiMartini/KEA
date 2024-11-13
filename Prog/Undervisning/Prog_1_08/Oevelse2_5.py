""" 
2.5 - sørg for at der er en metode i klassen der kan returnere temperaturen i kelvin grader (Celsius to Kelvin: K = C + 273.15).
"""

from machine import Pin
from time import sleep
from dht import DHT11

dht11=DHT11(Pin(0))

def cel_to_fah(temp_cel):
    return temp_cel*9/5+32

def cel_to_kel(temp_cel):
    return temp_cel+273.15


while True:
    measurement=dht11.measure()
    temp=dht11.temperature()
    hum=dht11.humidity()
    print(f"{temp} C")
    print(f"{cel_to_fah(temp)} F")
    print(f"{cel_to_kel(temp)} K")
    print(hum)
    sleep(0.5)