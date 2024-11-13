""" 
2.1
lav en ny fil kaldet "oevelse2_1.py" og importer DHT11 klassen fra sensor modulet. Lav en instans af klassen og sørg for at signal pin fra sensor er sat til GPIO 0. Lav en måling og print temperatur og luftfugtihed til shell.
"""

# A simple DHT11 test program
from machine import Pin
from time import sleep
from dht import DHT11


class dht11_class():
    description="Class to store temperature and humidity"

    def __init__(self,pin):
        self.pin=pin
        self.temperature=None
        self.humidity=None

    def set_temperature(self,measured_temp:float):
        self.temperature=measured_temp
    
    def set_humidity(self,measured_humi:float):
        self.humidity=measured_humi
        
    def set_pin(self,desired_pin:int):
        self.pin=desired_pin

def make_DHT11(InputObject):
    return DHT11(Pin(InputObject.pin))
##################
# OBJECTS
sensor=dht11_class(0)
sensor=DHT11(Pin(sensor.pin)) # The DHT11 object
# sensor=make_DHT11(int(sensor.pin))

while True:
    # Do the measurement
    sensor.measure()
    temp = sensor.temperature()     # Get the temperature
    # Print the result
    print(f'Temperatur: {temp}°C')
    hum = sensor.humidity()         # Get the humidity
    print(f'Fugtighed: {hum:.2f}%')
    
    sleep(1)                       # Wait 1 second, then loop around