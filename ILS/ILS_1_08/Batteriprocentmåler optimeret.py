from machine import ADC,Pin
from adc_sub import ADC_substitute
from time import sleep
import utime

# CONFIGURATION
pin_adc=34

# OBJECTS
adc=ADC_substitute(pin_adc)

while True:
    Spænding=adc.read_voltage()*2
    batteriprocent=((Spænding-3)/(4.2-3.0))*100
    print(batteriprocent)
    sleep(0.5)
    