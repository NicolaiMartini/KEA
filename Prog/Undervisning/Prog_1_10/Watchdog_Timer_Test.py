# Watchdog Timer
from machine import WDT, Timer

def reset_watchdog(obj): # Callback der feeder watchdog timeren
	print("Feeding the watchdog!")
	wdt.feed() # Her feedes wdt med metoden feed

wdt=WDT(timeout=2000) # Timeout på 2000 ms

timer_0=Timer(0) # ESP32 har 4 hardware Timers som kan anvendes
# Her initialiseres en periodisk timer som kalder reset_watchdog hver 1.5 sekund
timer_0.init(period=1500,mode=Timer.PERIODIC,callback=reset_watchdog)