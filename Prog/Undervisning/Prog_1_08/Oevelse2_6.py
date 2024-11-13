"""
2.6 prøv at lave en ny klasse til at udregne strøm, spænding, modstand og effekt, med ohms lov. 
Sørg for at lave en metode til hver udregning så klassen har 12 metoder I alt.
Udregningerne skal printes i shell når metoderne kaldes.
Lav en instans af klassen og test metoderne ved at kalde dem med forskellige argumenter.
"""
from math import sqrt
from random import randint
from time import sleep

class Ohms_Law:
    Description="This class is made to help calculate Ohms Law."
    def __init__(self):
        self.P=None
        self.U=None
        self.R=None
        self.I=None

    def PRI(self,R,I):
        print(R*I**2)
    def PUR(self,U,R):
        print(U**2/R)
    def PUI(self,U,I):
        print(U*I)
        
    def URI(self,R,I):
        print(R*I)
    def UPI(self,P,I):
        print(P/I)
    def UPR(self,P,R):
        print(sqrt(P*R))
    
    def RUI(self,U,I):
        print(U/I)
    def RPI(self,P,I):
        print(P/I**2)
    def RUP(self,U,P):
        print(U**2/P)
    
    def IUR(self,U,R):
        print(U/R)
    def IPR(self,P,R):
        print(sqrt(P/R))
    def IPU(self,P,U):
        print(P/U)

Ohm=Ohms_Law()

while True:
    Ohm.PRI(randint(2,20),randint(2,20))
    Ohm.PUR(randint(2,20),randint(2,20))
    Ohm.PUI(randint(2,20),randint(2,20))
    Ohm.URI(randint(2,20),randint(2,20))
    Ohm.UPI(randint(2,20),randint(2,20))
    Ohm.PUI(randint(2,20),randint(2,20))
    Ohm.RUI(randint(2,20),randint(2,20))
    Ohm.RPI(randint(2,20),randint(2,20))
    Ohm.RUP(randint(2,20),randint(2,20))
    Ohm.IUR(randint(2,20),randint(2,20))
    Ohm.IPR(randint(2,20),randint(2,20))
    Ohm.IPU(randint(2,20),randint(2,20))
    sleep(5)
