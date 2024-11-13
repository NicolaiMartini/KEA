# A simple ESP32 USB <-> UART <-> ESP 32 USB program
import sys, uselect
from machine import UART

# Configuration
uart_port=2 # ESP32 UART port
uart_speed=1000 # UART speed

# Info: USB speed 115200, 8N1

# OBJECTS
uart=UART(uart_port,uart_speed) # UART object creation, 8 bits, parity None, 1 stop bit
usb=uselect.poll() # Set up an input polling object
usb.register(sys.stdin,uselect.POLLIN) # Register polling object

print("ESP32 USB <-> UART <-> UART <-> USB 32 USB program")
print("Remember to connect TX1 -> RX2 and RX1 <- TX2")
print("Type something on the keyboard \n")

while True:
    # Receive data from the UART
    if uart.any()>0:
        string=uart.readline().decode() # UART returns bytes. They have to be conv. to chars/a string
        print(string,end="") # Echo received data to shell
    if usb.poll(0):
        string=sys.stdin.readline() # Read one line at a time
        sys.stdin.readline() # WEIRD! - Needed to avoid a second handling of the same input
        uart.write(string) # Send the USB data to UART