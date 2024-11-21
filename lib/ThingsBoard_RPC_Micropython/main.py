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
from sys import exit
import gc
import secrets

# the handler callback that gets called when there is a RPC request from the server
def handler(req_id, method, params):
    """handler callback to recieve RPC from server """
     # handler signature is callback(req_id, method, params)
    print(f'Response {req_id}: {method}, params {params}')
    print(params, "params type:", type(params))
    try:
        # check if the method is "toggle_led1" (needs to be configured on thingsboard dashboard)
        if method == "toggle_led1":
            # check if the value is is "led1 on"
            if params == True:
                print("led1 on")
            else:
                print("led1 off")
        # check if command is send from RPC remote shell widget   
        if method == "sendCommand":
            print(params.get("command"))

    except TypeError as e:
        print(e)

# see more about ThingsBoard RPC at the documentation:
# https://thingsboard.io/docs/user-guide/rpc/
        
# See examples for more authentication options
# https://github.com/thingsboard/thingsboard-micropython-client-sdk/
client = TBDeviceMqttClient(secrets.SERVER_IP_ADDRESS, access_token = secrets.ACCESS_TOKEN)


# Connecting to ThingsBoard
client.connect()
print("connected to thingsboard, starting to send and receive data")
while True:
    try:
        print(f"free memory: {gc.mem_free()}")
        # monitor and free memory
        if gc.mem_free() < 2000:
            print("Garbage collected!")
            gc.collect()
        
        # uncomment for sending telemetry from device to server       
        
        #telemetry = {}
        #client.send_telemetry(telemetry)
        
        #callback to get server RPC requests
        client.set_server_side_rpc_request_handler(handler) 
        
        # Checking for incoming subscriptions or RPC call requests (non-blocking)
        client.check_msg()
        sleep(3) # blocking delay
    except KeyboardInterrupt:
        print("Disconnected!")
        # Disconnecting from ThingsBoard
        client.disconnect()
        exit()
