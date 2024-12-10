# A simple potmeter test program
from machine import ADC, Pin, PWM
from time import sleep

potmeter_adc = ADC(Pin(34))
potmeter_adc.atten(ADC.ATTN_11DB)      # Full range: 3,3 V and 12 bits

adc1 = 2390
U1 = 4.1
adc2 = 2080
U2 = 3.6

a = (U1-U2)/(adc1-adc2)
b = U2 - a*adc2

def batt_voltage(adc_v):
    u_batt = a*adc_v+b
    return u_batt

#Procent:
# 3V = 0%
# 4.2V = 100%
def batt_percentage(u_batt):
    without_offset = (u_batt-3)
    normalized = without_offset / (4.2-3.0)
    percent = normalized * 100
    return percent

while True:
    val = potmeter_adc.read()
    print('ADC value:',val)
    print('U_adc', (3.3/4096*val))
    print('U_batt', batt_voltage(val))
    print('U percentage', batt_percentage(batt_voltage(val)))
    print('*'*10)
    sleep(0.2)
