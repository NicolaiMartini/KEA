from machine import ADC, Pin, PWM
from time import sleep

potmeter_adc=ADC(Pin(34))
potmeter_adc.atten(ADC.ATTN_11DB)

print("Potmeter test, PWM on LED1\n")

U2=4 # Y2
adc2 = 2175 # x2
U1 = 3 #y1
adc1 = 1590 #x1

a=(U2-U1)/(adc2-adc1) #0.0016-0.0017
b=U2-a*adc2 # 0.3

def batt_voltage(adc_val):
    u_batt=a*adc_val + b
    return u_batt

def batt_percentage(u_batt):
    without_offset = u_batt-3.0
    normalized = without_offset / 1.2 # 4.2V-3.0V = 1.2V
    percentage = normalized*100
    return percentage

while True:
    val=potmeter_adc.read()
    print(val)

    U_adc = val*3.3/4096
    U_batt=batt_voltage(val)
    Batt_percentage = batt_percentage(U_batt)
    if Batt_percentage>100:
        Batt_percentage=100
    elif Batt_percentage<0:
        print('Batteri might be broken')
        Batt_percentage=0
    print(f"Battery percentage: {Batt_percentage}")
    sleep(0.2)