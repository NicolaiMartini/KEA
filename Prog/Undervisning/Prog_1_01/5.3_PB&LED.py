from machine import Pin
from time import sleep

PB1 = Pin(4, Pin.IN)
LED1 = Pin(26, Pin.OUT)

button_presses=0
while True:
#     print("Knap værdi: ", PB1.value()) # Activate this line to display button value (0 or 1) - Can also be deleted.
    first=PB1.value()
    sleep(0.01)
    second=PB1.value()
    if first==1 and second==0:
        button_presses+=1
        print(f"The button has been pressed {button_presses} times.")