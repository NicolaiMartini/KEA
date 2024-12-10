# A simple LMT87 test program
from time import sleep
from lmt87 import LMT87

#####
# CONFIGURATION
pin_lmt87=35

# Calibration Values
t1 = 25.2
adc1 = 2659
t2 = 24.2
adc2 = 2697

#####
# OBJECTS
temp=LMT87(pin_lmt87)

#####
# PROGRAM

print("LMT87 test\n")

print(temp.calibrate(t1, adc1, t2, adc2))

while True:
	adc_val = temp.get_adc_value()
	temperature = temp.get_temperature()
	print("Temp: %d °C <- %d" % (temperature, adc_val))
	
	sleep(1)