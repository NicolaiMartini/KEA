"""
Øvelse 4 – Oplad el-cykel når der billig el og klimavenlig energi 

Brug eksemplet fra øvelse 1 så der forbindes til wifi når systemet bootes op. 

Tjek hvert 5. sekund om der er grøn energi. Hvis der er grøn energi så sørg for at Neopixel LED4 lyser grønt. Og hvis der ikke er grøn energi skal LED4 lyse rødt. 

Prøv at sætte jeres relæ til Educaboardet og tænd det når der er grøn energi og sluk det når der ikke er grøn energi. (Relæ kan tænde og slukke en ladestation) 

Prøv at opdatere programmet, så at el prisen skal være lav (du bestemmer selv pris) og der skal være grøn energi for at den skal tænde relæet. 

Test ved at lave en dictionary der svarer til det data der kommer tilbage fra API-kaldet og prøv at ændre værdierne (over og under den valgte tærsken) I den for at se om løsningen virker. På denne måde behøver man ikke vente på at den rigtige data fra API'en ændrer sig. 

Prøv at opdatere LCD display på Educaboard så man kan se den nuværende gram CO2 pr. kwh strøm og elprisen, hver gang der laves et API kald.
"""
from machine import Pin, reset
from time import ticks_ms,ticks_diff
from neopixel import NeoPixel
import requests

#####
# Pins
relay=Pin(14,Pin.OUT)
neopixel=NeoPixel(Pin(26,Pin.OUT),1)

#####
# Objects
response=requests.get(url="https://api.energidataservice.dk/dataset/Elspotprices?limit=2")
ticker=ticks_ms()

#####
# Functions
def green_np():
    neopixel[0]=(0,55,0)
    neopixel.write()

while True:
     try:
         relay.value(not relay.value())
         if ticks_diff(ticks_ms(),ticker)>1000:
#             response=response.json().get("records")[1].get("SpotPriceDKK") # Requires internet
            print(f"The price is: {response}")
            if response<850:
                green_np()
            
            ticker=ticks_ms()
     except KeyboardInterrupt:
         reset()