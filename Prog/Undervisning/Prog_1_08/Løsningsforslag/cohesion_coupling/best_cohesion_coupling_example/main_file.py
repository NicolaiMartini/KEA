import time

from neopixel_ring import NeoPixelRing
from button import Button
from potentiometer import Potentiometer
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

kopier kodeeksemplet ind i en ny mappe kaldet "best_cohesion_and_coupling_example"

2. pr�v derefter at skabe low coupling ved at lave et nyt modul til hver klasse (trykknap, neopixel-ring, potmeter)
    - Gem hver klasse med korrekt navngivning i et modul for sig
    - S�rg for at de n�dvendige klasser importeres i hvert modul
    - Opret derefter en main fil og importer hver modul derinde og lav et objekt fra hver klasse
        (et til potmeter, og et til neopixel-ring og et til hver trykknap)
    - s�rg for at main filen starter main() funktionen og test at koden fungerer
    - gem main filen i mappen "best_cohesion_and_coupling_example", og navngiv den "main_file.py"
    - lav en lib mappe inde i denne mappe og inds�t de klasserne til neopixel-ringen, potmeteret og tryknapperne deri

"""

def main():
    np_ring = NeoPixelRing(26, 12)
    pot = Potentiometer(34)

    def button1_handler(pin):
        np_ring.set_color((0, 255, 0))
        time.sleep(1)

    def button2_handler(pin):
        np_ring.set_color((0, 0, 255))
        time.sleep(1)

    button1 = Button(0, button1_handler)
    button2 = Button(4, button2_handler)

    while True:
        pot_value = pot.read_value()
        brightness = pot_value // 4
        np_ring.set_color((brightness, 0, 0))
        time.sleep(0.1)

if __name__ == "__main__":
    main()