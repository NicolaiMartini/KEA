from machine import Pin
from time import sleep

GREEN_PIN=13
LED3=Pin(GREEN_PIN, Pin.OUT)
LED3.off()

while True:
    LED3.value(not LED3.value())
    sleep(0.01) # Largest interval before "blinking" becomes non-stop lighting.
