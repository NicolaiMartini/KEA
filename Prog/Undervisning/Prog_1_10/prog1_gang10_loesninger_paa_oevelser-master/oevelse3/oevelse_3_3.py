from machine import RTC, Timer
"""
3.3 - Prøv at lave et program der bruger RTC til at tjekke
om datetime() er på 22. sekund, og kald derefter en funktion
der printer ”triggered” og rtc.datetime()og sørg derefter for
at den kun bliver triggered én gang. 
    brug Timer til at kalde en funktion hvert 900 millisekund hvor
    funktionen tjekker om datetime() sekunder er == 22 og printer
    “triggered” og datetime() når den er True
https://docs.micropython.org/en/latest/esp32/quickref.html#timers
"""
rtc = RTC()
def datetime_trigger(obj):
    print(rtc.datetime())
    if rtc.datetime()[6] == 22:
        print("Triggered", rtc.datetime())
        timer_0.deinit() #  deinitialisere timer objekt så den ikke trigges igen

timer_0 = Timer(0)
timer_0.init(period=1000, mode=Timer.PERIODIC, callback=datetime_trigger)