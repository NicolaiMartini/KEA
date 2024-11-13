from machine import Pin
from time import sleep
import dht

########################################
# CONFIGURATION
dht11_pin = 0

########################################
# OBJECT
dht11 = dht.DHT11(Pin(dht11_pin))

########################################
# PROGRAM
def cel_to_fah(temp_Cel):
    return temp_Cel*9/5+32

while True:
    dht11.measure() #Make the measurement
    temp = dht11.temperature() #Get the temperature
    hum = dht11.humidity() #Get the humidity
    temp_fah=cel_to_fah(temp)
    print("Temperatur: %3d °C" % temp)
    print("Fugtighed : %3d %%" % hum)
    print(f"Fahrenheit: {temp_fah}")
    
    sleep(1)