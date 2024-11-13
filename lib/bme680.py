# Complete project details at https://RandomNerdTutorials.com/micropython-bme680-esp32-esp8266/

from machine import Pin, I2C
from time import sleep
from bme680_i2c import *

#########################################################################
# CONFIGURATION
i2c_port = 0

#########################################################################
# OBJECTS
i2c = I2C(i2c_port)

bme = BME680_I2C(i2c = i2c)

#########################################################################
# PROGRAM
while True:
  try:
    print("Temperature: %0.1f °C" % round(bme.temperature))
    print("Humidity   : %0.0f %%" % round(bme.humidity))
    print("Pressure   : %0.0f hPa" % round(bme.pressure))
    print("Gas        : %0.0f kΩ" % round(bme.gas / 1000))
    print("------------------")
  except OSError as e:
    print("Failed to read sensor.")
 
  sleep(1)
