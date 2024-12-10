from mpu6050 import MPU6050
from time import sleep
from machine import Pin, I2C
from neopixel import NeoPixel

n = 12 #Neopixelring på pin 12
np = NeoPixel(Pin(12, Pin.OUT), n)

i2c = I2C(0)
imu = MPU6050(i2c)

def set_color(r, g, b):
    for i in range(n):
        np[i] = (r, g, b)
    np.write()

while True:
    values = imu.get_values()
    if  values["acceleration z"] < -15000: # Tænder for bremselys
        set_color(20, 0, 0)
        sleep(1) #Hvor lang tid bremselyset er tændt
    else:
        set_color(0, 0, 0)
    print(values["acceleration z"])
    sleep(0.05) #Tid for hvert tjek, medmindre bremselys tænder
    