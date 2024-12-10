from machine import UART # Import UART class from machine module
uart2=UART(2,baudrate=9600) # Initiate the UART-connection.
# UART2 from the hardware-manufacturer. Pins are TX=17 and RX=16.
uart2 # Call the UART, see the associated informations.

# Use uart2.write('write your string here')
# Other connected device can then read with the following line.
# uart2.read()