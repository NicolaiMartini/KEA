# # A simple potmeter test program
# from machine import ADC, Pin, PWM
# from time import sleep
# 
# #####
# # CONFIGURATION
# pin_potmeter=34
# 
# #####
# # OBJECTS
# potmeter_adc = ADC(Pin(pin_potmeter))
# potmeter_adc.atten(ADC.ATTN_11DB) # Full range: 3.3V, 12 bits
# 
# #####
# # PROGRAM
# print("ADC and potmeter test\n")
# 
# while True:
# 	adc_val = potmeter_adc.read()
# 	print(adc_val)
# 	
# 	sleep(0.2)

# ADC_SUB code
from machine import ADC, Pin, PWM
from time import sleep
from adc_sub import ADC_substitute

#####
# CONFIGURATION
pin_potmeter=34

#####
# OBJECTS
adc=ADC_substitute(pin_potmeter)

#####
# PROGRAM
print("ADC and potmeter test\n")

while True:
    print(adc.read_voltage())
    sleep(0.2)
