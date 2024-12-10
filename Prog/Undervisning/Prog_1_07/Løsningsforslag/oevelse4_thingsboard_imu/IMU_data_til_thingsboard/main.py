# -*- coding: utf-8 -*-
#
# Copyright 2024 Kevin Lindemark
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

from uthingsboard.client import TBDeviceMqttClient
from time import sleep
from machine import I2C
import sys
import gc
import secrets
from mpu6050 import MPU6050

#Initialisering af I2C objekt
i2c = I2C(0)     
#Initialisering af mpu6050 objekt
imu = MPU6050(i2c)
                                        # Make client object to connect to thingsboard
client = TBDeviceMqttClient(secrets.SERVER_IP_ADDRESS, access_token = secrets.ACCESS_TOKEN)
client.connect()                           # Connecting to ThingsBoard
print("connected to thingsboard, starting to send and receive data")
while True:
    try:
        print(f"free memory: {gc.mem_free()}") # monitor memory left
        
        if gc.mem_free() < 2000:          # free memory if below 2000 bytes left
            print("Garbage collected!")
            gc.collect()                  # free memory 
        imu_data = imu.get_values()
        # store telemetry in dictionary 
        telemetry = {"acceleration_x" : imu_data["acceleration x"],
                     "acceleration_y" : imu_data["acceleration y"],
                     "acceleration_z" : imu_data["acceleration z"],
                     "temperature_celsius" : imu_data["temperature celsius"],
                     "gyroscope_x" : imu_data["gyroscope x"],
                     "gyroscope_y" : imu_data["gyroscope y"],
                     "gyroscope_z" : imu_data["gyroscope z"],
                     
                     }                   
        client.send_telemetry(telemetry) #Sending telemetry  
        sleep(1)                          # send telemetry once every second
    except KeyboardInterrupt:
        print("Disconnected!")
        client.disconnect()               # Disconnecting from ThingsBoard
        sys.exit()                        # Stop program

        