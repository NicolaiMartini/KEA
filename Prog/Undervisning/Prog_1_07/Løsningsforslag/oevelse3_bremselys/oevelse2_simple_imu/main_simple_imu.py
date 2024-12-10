from mpu6050 import MPU6050
from time import sleep
from machine import Pin, I2C
from neopixel import NeoPixel

n = 2
np = NeoPixel(Pin(26, Pin.OUT), n)

i2c = I2C(0)
imu = MPU6050(i2c)

def set_color(r, g, b):
    for i in range(n):
        np[i] = (r, g, b)
    np.write()

while True:
    values = imu.get_values()
    if  values["acceleration z"] < -15000:
        set_color(100, 0, 0)
        sleep(1)
    else:
        set_color(0, 0, 0)
    print(values["acceleration z"])
    sleep(0.05)
    