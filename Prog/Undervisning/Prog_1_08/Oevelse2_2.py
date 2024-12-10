""" 
2.2 - lav en ny fil kaldet "oevelse2_2.py" opdater klassen fra forgående slide såder er en metode der kan returnere temperaturen i Fahrenheit grader (Celsius to Fahrenheit: F = C x 9/5 + 32)
"""

from machine import Pin
from time import sleep
from dht import DHT11

dht11=DHT11(Pin(0))

def cel_to_fah(temp_cel):
    return temp_cel*9/5+32


while True:
    measurement=dht11.measure()
    temp=dht11.temperature()
    hum=dht11.humidity()
    print(temp)
    print(cel_to_fah(temp))
    print(hum)
    sleep(0.5)