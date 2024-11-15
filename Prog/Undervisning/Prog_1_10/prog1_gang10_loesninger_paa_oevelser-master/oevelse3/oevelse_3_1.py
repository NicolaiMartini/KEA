from machine import WDT, Timer
"""3.1 - Prøv eksemplet med watchdog timer og prøv at ændre
watchdog time_0 til at vente 2100 ms for at se den i aktion"""
def reset_watchdog(obj): #  callback der feeder watchdog timeren
    print("Feeding the watchdog!")
    wdt.feed() #  her feedes wdt med metoden feed

wdt = WDT(timeout=2000) # timeout på 2000 ms

timer_0 = Timer(0) # ESP32 har 4 hardware Timers som kan anvendes
# her initialiseres en periodisk timer som kalder reset_watchdog hver 1.5 sekund
timer_0.init(period=2100, mode=Timer.PERIODIC, callback=reset_watchdog)
