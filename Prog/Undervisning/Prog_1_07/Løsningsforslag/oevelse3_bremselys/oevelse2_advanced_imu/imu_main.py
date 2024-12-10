from imu import MPU6050  # https://github.com/micropython-IMU/micropython-mpu9x50
import time
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

# Temperature display
print("Temperature: ", round(imu.temperature,2), "°C")

while True:
    # reading values
    acceleration = imu.accel
    gyroscope = imu.gyro  
    print ("Acceleration x: ", round(acceleration.x,2), " y:", round(acceleration.y,2),
           "z: ", round(acceleration.z,2))
    if acceleration.z < -1.9:
        set_color(100, 0, 0)
        time.sleep(0.2)
    else:
        set_color(0, 0, 0)
    




    
    #time.sleep(0.2)