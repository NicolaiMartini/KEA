from machine import Timer, Pin
"""
3.2 - Lav en hardware Timer med en callback-funktion
der periodisk toggler en LED hvert 100 millisekund
"""
led1 = Pin(26, Pin.OUT)
timer_0 = Timer(0)

def toggle_led1(obj):
    led1.value(not led1.value())
    
timer_0.init(period=100, mode=Timer.PERIODIC, callback=toggle_led1)