# Mål U
#     Udskriv i Thonny
#     Også udskriv ADC og U_ADC

from machine import ADC,Pin
from adc_sub import ADC_substitute
from time import sleep
import utime

#####
# CONFIGURATION
pin_adc=34

#####
# OBJECTS
adc=ADC_substitute(pin_adc)

# while True:
#     adc_målt=adc.read_adc()
#     reel_adc=adc_målt*2
#     print(f"Spænding: {adc.read_voltage()}")
#     print(f"Målt ADC: {adc_målt}")
#     print(f"Reel adc: {reel_adc}")
#     utime.sleep_ms(100)




# # Lave førstegradsligning der udregner batteriprocent
# # 3.0V = 0% batteriprocent, 4.2V = 100% batteri
# 
# ## Førstegradsligning
# ### Hent U og ADC_value fra USB PSU
# Dataset_one=(2.1,4095)
# Dataset_two=(1.5,0)
# # 
# # ### Find a
# a=(Dataset_two[0]-Dataset_one[0])/(Dataset_two[1]-Dataset_one[1])
# # print(f"a={a}")
# # 
# # ### Find b
# b=(Dataset_one[0]-a*Dataset_one[1])
# print(f"b = {b}")
# ### b=(Dataset_two[0]-a*Dataset_two[1])
# print(f"Førstegradsligning:\n y={a}x+{b}")


# Skriv program der måler batteriprocent
#     Udskriv i Thonny
#     Udskriv også U_ADC og U
while True:
    adc_målt=adc.read_adc()
    reel_adc=adc_målt*2
    print(f"Spænding: {adc.read_voltage()}")
    print(f"Målt ADC: {adc_målt}")
    print(f"Reel adc: {reel_adc}")
    Førstegradsligning=0.0001465201*adc_målt+1.5
    print(f"FørstegradsligningV: {Førstegradsligning}V")
    SpændingUd=adc.read_voltage()*2
    batteri=SpændingUd
    print(SpændingUd)
    batteriprocent=((SpændingUd-3)/1.2)*100
    print(batteriprocent)
    sleep(0.5)