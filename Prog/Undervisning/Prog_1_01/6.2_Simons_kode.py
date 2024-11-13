from machine import Pin

PB1=Pin(4,Pin.IN,Pin.PULL_UP)
LED1=Pin(26,Pin.OUT)
def toggle_led(Pin):
    LED1.value(not LED1.value())
    
PB1.irq(trigger=Pin.IRQ_FALLING, handler=toggle_led)