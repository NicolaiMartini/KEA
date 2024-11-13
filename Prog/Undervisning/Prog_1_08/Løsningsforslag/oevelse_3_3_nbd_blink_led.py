from machine import TouchPad, Pin
from time import ticks_ms
"""
prog #8 - øvelse 3.1 - 3.3
3.1 - Tilslut dupont kabel til GPIO 0 og lav et TouchPad objekt til den pin.
Lav et uendeligt while loop hvor at led1 blinkes med et non-blocking delay på 500ms ved hjælp af ticks_ms.
LED1 skal kun blinke imens dupontkablet med touch berøres.​

3.2 - Tilføj kode så de sidste 2 LED’er også sættes til at blinke når de touchPad()
GPIO’s som er forbundet til dem bliver berørt. Brug GPIO 14 og 15 og opret et TouchPad objekt til hver af dem. ​

Dette skal ligeledes være med non-blocking delays
(husk at forbinde dupont kabler fra LED2, og LED3 til port expander ben på educaboard)
JP6 GP2 → MISO og GP3 → MOSI på JP1

3.3 - Prøv at sæt duponterne som er tilslutte touchPad GPIO’erne i et ledende materiale fx. frugt, eller metal:
det vil resultere i at genstanden bliver et touch interface :)
"""


# på educaboard kan pin 0, 14, 15 bruges til touch
touch1 = TouchPad(Pin(0, Pin.IN))
touch2 = TouchPad(Pin(15, Pin.IN))
touch3 = TouchPad(Pin(14, Pin.IN))

led1 = Pin(26, Pin.OUT)
led1_start = ticks_ms()
led1_period = 500¨å
# husk at forbind educaboard pins til LED2 og LED3 med dupont kabler
led2 = Pin(12, Pin.OUT) # JP6 GP2 → MISO
led2_start = ticks_ms()
led2_period = 800

led3 = Pin(13, Pin.OUT) # GP3 → MOSI på JP1
led3_start = ticks_ms()
led3_period = 1100

while True:
    if touch1.read() < 150:
        if ticks_ms() - led1_start > led1_period:
            led1.value(not led1.value())
            led1_start = ticks_ms()
        
    if touch2.read() < 150:
        if ticks_ms() - led2_start > led2_period:
            led2.value(not led2.value())
            led2_start = ticks_ms()
        
    if touch3.read() < 150:
        if ticks_ms() - led3_start > led3_period:
            led3.value(not led3.value())
            led3_start = ticks_ms()