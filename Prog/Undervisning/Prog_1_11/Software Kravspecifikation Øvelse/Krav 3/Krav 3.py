"""
OMDØB DENNE FIL TIL main.py NÅR DEN UPLOADES TIL EDUCABOARD ESP32
"""

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
from time import sleep, ticks_ms, ticks_diff
from machine import reset, ADC, Pin, PWM
import gc
import secrets
                                           # Make client object to connect to thingsboard

ticker=ticks_ms()

# Pins
potmeter_adc=ADC(Pin(34))
potmeter_adc.atten(ADC.ATTN_11DB)

### 
# Battery functions
# Linear function for batt-% calculations
adc1=2390
U1=4.1
adc2=2080
U2=3.6
a=(U1-U2)/(adc1-adc2)
b=U2-a*adc2

# Batt voltage
def batt_voltage(adc_v):
    u_batt=a*adc_v+b
    return u_batt

# Batt % based on voltage
# 3V = 0%
# 4.2V = 100%
def batt_percentage(u_batt):
    without_offset=(u_batt-3)
    normalized=without_offset/(4.2-3.0)
    percent=normalized*100
    return percent

def batteri_percent
    val=potmeter_adc.read()
    batteri_percentage_calc=batt_percentage(batt_voltage(val))
# Thingsboard connection
client = TBDeviceMqttClient(secrets.SERVER_IP_ADDRESS, access_token = secrets.ACCESS_TOKEN)
client.connect()                           # Connecting to ThingsBoard
print("connected to thingsboard, starting to send and receive data")

###

# Main program
while True:
    try:
        print(f"free memory: {gc.mem_free()}") # monitor memory left
        if gc.mem_free() < 2000:          # free memory if below 2000 bytes left
            print("Garbage collected!")
            gc.collect()                  # free memory 
        if ticks_diff(ticks_ms(),ticker)>5000: # 5s non-blocking delay
            telemetry = {"Battery Percentage" : batteri_percent}                # store telemetry in dictionary     
            client.send_telemetry(telemetry) #Sending telemetry
            ticker=ticks_ms()
    except KeyboardInterrupt:
        print("Disconnected!")
        client.disconnect()               # Disconnecting from ThingsBoard
        reset()                           # reset ESP32

