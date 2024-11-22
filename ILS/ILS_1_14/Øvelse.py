"""
A simple ESP32<->UART remote data system incl EEPROM and INA219 use
"""
from machine import I2C, UART, Pin, reset
from ina219_lib import INA219
from eeprom_24xx64 import EEPROM_24xx64
from time import ticks_ms, sleep
import dht

#####
# Configuration
# PB
pb_pin=27
dht11_pin=19

#####
# OBJECTS
pb=Pin(pb_pin,Pin.IN,Pin.PULL_UP)
dht=dht.DHT11(Pin(dht11_pin))

# I2C: EEPROM and INA219
eeprom=EEPROM_24xx64(I2C(0),0x50) # The EEPROM object
ina219=INA219(I2C(0),0x40) # The INA219 object

#####
# FUNCTIONS
# Return Celsius, C
def temp():
    dht.measure()
    tempC=dht.temperature()
    temperature=f"{tempC}"
    return temperature

# Return, Humidity, %
def hum():
    dht.measure()
    hum=dht.humidity()
    humidity=f"{hum}%"
    return humidity

def ina_current():
    maaling=str(ina219.get_current())
    return maaling

#####
# PROGRAN
print("Two-way ESP32 remote data system\n")

ticker=ticks_ms()
ina219.set_calibration_16V_400mA() # Set a more sensitive range
filename="data.csv"

while True:
    pb1=pb.value()
    sleep(0.01)
    pb2=pb.value()
    if pb1==1 and pb2==0:
        with open(filename,"a+") as file:
            file.write("Time:,Current:,Temp:\n") # Set header in the file
        while True:
            if ticks_ms()-ticker>250:
                print(ticks_ms())
                ticker=ticks_ms()
                with open(filename, "a+") as file:
                    file.write(str(ticker)+","+ina_current()+","+temp()+" \n")
    elif KeyboardInterrupt:
        reset() # Reset ESP32
        