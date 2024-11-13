from time import ticks_ms
from neopixel import NeoPixel
from machine import Pin

PIXELS = 2
NP_PIN = 26
np = NeoPixel(Pin(NP_PIN), PIXELS)

toggle =  {
        "toggle_led4" : True,
        "toggle_led5" : True,
           }

def toggle_led4():
    
    if toggle["toggle_led4"]:
        np[0] = (100, 100, 100)
        toggle["toggle_led4"] = False
    else:
        np[0] = (0, 0, 0)
        toggle["toggle_led4"] = True
    np.write()


def toggle_led5():
    
    if toggle["toggle_led5"]:
        np[1] = (0, 100, 0)
        toggle["toggle_led5"] = False
    else:
        np[1] = (0, 0, 0)
        toggle["toggle_led5"] = True
    np.write()
        

class NonBlockingTimer:
    
    def __init__(self, delay_period_ms):
        """ delay_period_ms is milliseconds delay between
            each function call
        """
        self.start_time = ticks_ms()
        self.delay_period_ms = delay_period_ms
    
    def non_blocking_timer(self, func):
        """
            takes func reference as argument
        """
        if ticks_ms() - self.start_time > self.delay_period_ms:
            func() # laver funktionskald når tiden er gået
            self.start_time = ticks_ms() # genstarter tiden

led4_timer = NonBlockingTimer(1000)
led5_timer = NonBlockingTimer(100)
# Man kan lave en ny funktion til hver opgave der skal køres med et bestemt interval

     
while True:
    # her erstattes func med time_is_up funktionen som kaldes hver gang tiden er gået
    led4_timer.non_blocking_timer(toggle_led4)
    led5_timer.non_blocking_timer(toggle_led5)
    
