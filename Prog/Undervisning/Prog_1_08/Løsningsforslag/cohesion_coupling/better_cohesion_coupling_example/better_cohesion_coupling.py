import machine
import neopixel
import time

"""
Problemer med dette design:

Lav cohesion:

Klassen AllInOne har for mange ansvarsomr�der
(LED-kontrol, potentiometer-l�sning, og knaph�ndtering),
hvilket g�r den sv�r at forst� og vedligeholde.

H�j coupling:

Alle komponenter er t�t forbundet inden for samme klasse,
hvilket g�r det sv�rt at �ndre eller teste individuelle dele af systemet.

�velse:

koden skal omstruktureres (re-formateres).
Det meste af koden fra eksemplet kan genbruges for at l�se �velsen, men det skal flyttes rundt.

1. pr�v at skabe h�j cohesion ved at oprette en ny klasse til hvert ansvarsomr�de
    - Navngiv hver klasse fornuftigt efter PEP8: https://www.python.org/dev/peps/pep-0008
    - Hver klasse skal have sin egen constructor (__init__) og instantiere de objekter der
        kr�ves for at den kan fungere.
    - Lav nu et objekt for hver af klasserne, til potmeter, neopixel-ring og et til hver trykknap.
    - Behold hver klassse i samme fil og test at koden virker
    - Gem dette program i en mappe kalde "better_cohesion" og navngiv filen "better_cohesion_example.py"


"""

###########################################################################
# Nye klasser inds�ttes her

class Potmeter:
    def __init__(self, pot_pin):
        self.pot = machine.ADC(machine.Pin(pot_pin))
        self.pot.atten(machine.ADC.ATTN_11DB)
        self.pot.width(machine.ADC.WIDTH_10BIT)
    
    def read(self):
        return self.pot.read()


class NeopixelRing:
    def __init__(self, led_pin, num_pixels):
        self.np = neopixel.NeoPixel(machine.Pin(led_pin), num_pixels)
        self.num_pixels = num_pixels
    
    def set_color(self, r, g, b):
        for i in range(self.num_pixels):
            self.np[i] = (r, g, b)
        self.np.write()
        
        
class Button:
    def __init__(self, button_pin, button_handler):
        self.button = machine.Pin(button_pin, machine.Pin.IN, machine.Pin.PULL_UP)
        self.button_handler = button_handler
        self.button.irq(trigger=machine.Pin.IRQ_FALLING, handler=self.button_handler)



    
###########################################################################



npr = NeopixelRing(26, 12)
def button1_handler(pin):
    npr.set_color(0, 0, 100)
    time.sleep(0.2)

button1 = Button(4, button1_handler)

def button2_handler(pin):
    npr.set_color(0, 100, 0)
    time.sleep(0.2)
    
button2 = Button(0, button2_handler)    
    

pot = Potmeter(34)
while True:
    
    brightness = pot.read() // 4
    npr.set_color(brightness, 0, 0)
    time.sleep(0.1)


