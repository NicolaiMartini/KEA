from machine import Pin
from time import sleep

PB1=Pin(4,Pin.IN) # Instantiate Pin object
LED1=Pin(26,Pin.OUT) # Instantiate Red LED
LED1.value(1) # Red ON to show program is running
LED2=Pin(12,Pin.OUT) # Instantiate Yellow LED
LED2.value(1) # Make sure Yellow starts with OFF-state

while True:
    # Call value() method of Pin object
    # Save the result in a variable
    first=PB1.value()
    sleep(0.01)
    second=PB1.value()
    # If button switches from unpressed (1) to pressed (0)
    if first==1 and second==0:
        print("The button is pressed.")
        LED2.value(not LED2.value()) # Switch LED2-state when button is pressed
        # This block of code runs when the button is pressed
        
    # If the button switches fromw pressed (0) to unpressed (1)
    if first==0 and second==1:
        print("The button is released.")
