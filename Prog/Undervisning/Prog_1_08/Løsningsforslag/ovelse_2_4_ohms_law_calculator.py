from math import sqrt

"""
prog #8 - Øvelse 2.4

​prøv at lave en ny klasse til at udregne​

strøm, spænding, modstand og effekt, med ohms lov.​

Sørg for at lave en metode til hver udregning så klassen har 12 metoder I alt.​

Udregningerne skal printes i shell når metoderne kaldes.​

Lav en instans af klassen og test metoderne ved at kalde dem med forskellige argumenter.​

​
"""

class OhmsLawCalculator:
    """class to calculate voltage, power, current and resistance with ohms law"""
    
    def __init__(self, current=None, voltage=None, power=None, resistance=None):
        self.current = current
        self.voltage = voltage
        self.power = power
        self.resistance = resistance
  
    def calculate_voltage_from_current_and_resistance(self, current=None, resistance=None):
        if current != None and resistance != None:
            print(f"Voltage is {current * resistance}V")
            self.voltage = current * resistance
        else:
            print("Please provide current and resistance!")
    
    def calculate_voltage_from_power_and_current(self, power=None, current=None):
        if power != None and current != None:
            print(f"Voltage is {power / current}V")
            self.voltage = power / current
        else:
            print("Please provide power and current!")
            
    def calculate_voltage_from_power_and_resistance(self, power=None, resistance=None):
        if power != None and resistance != None:
            print(f"Voltage is {sqrt(power * resistance)}V")
            self.voltage = sqrt(power * resistance)
        else:
            print("Please provide power and resistance!")            
    
    def calculate_power_from_current_and_voltage(self, current=None, voltage=None):
        if current != None and voltage != None:
            print(f"Power is {current * voltage}W")
            self.power = current * voltage
        else:
            print("Please provide current and voltage!")
            
    def calculate_power_from_voltage_and_resistance(self, voltage=None, resistance=None):
        if voltage != None and resistance != None:
            print(f"Power is {voltage ** 2 / resistance}W")
            self.power = voltage ** 2 / resistance
        else:
            print("Please provide voltage and resistance!")
            
    def calculate_power_from_resistance_and_current(self, resistance=None, current=None):
        if resistance != None and current != None:        
            print(f"Power is {resistance * current ** 2}W")
            self.power = resistance * current ** 2
        else:
            print("Please provide resistance and current!")
                    
    def calculate_resistance_from_voltage_and_current(self, voltage=None, current=None):
        if voltage != None and current != None:  
            print(f"Resistance is {voltage / current}Ω")
            self.resistance = voltage / current
        else:
            print("Please provide voltage and current!")
            
    def calculate_resistance_from_power_and_current(self, power=None, current=None):
        if power != None and current != None:  
            print(f"Resistance is {power / current**2}Ω")
            self.resistance = power / current**2
        else:
            print("Please provide power and current!")
            
    def calculate_resistance_from_voltage_and_power(self, voltage=None, power=None):
        if voltage != None and power != None:  
            print(f"Resistance is {voltage**2 / power}Ω")
            self.resistance = voltage**2 / power
        else:
            print("Please provide voltage and power!")
            
    def calculate_current_from_power_and_resistance(self, power=None, resistance=None):
        if power != None and resistance != None:  
            print(f"Current is {sqrt(power/resistance)}A")
            self.current = sqrt(power / resistance)
        else:
            print("Please provide power and resistance!")
            
    def calculate_current_from_power_and_voltage(self, power=None, voltage=None):
        if power != None and voltage != None:  
            print(f"Current is {power/voltage}A")
            self.current = power/voltage
        else:
            print("Please provide power and voltage!")
            
    def calculate_current_from_voltage_and_resistance(self, voltage=None, resistance=None):
        if voltage != None and resistance != None:  
            print(f"Current is {voltage / resistance}A")
            self.current = voltage / resistance
        else:
            print("Please provide voltage and resistance!")
    

ohms_law = OhmsLawCalculator()

ohms_law.calculate_voltage_from_current_and_resistance(current=0.3, resistance=10)
ohms_law.calculate_power_from_current_and_voltage(current=10, voltage=50)
ohms_law.calculate_resistance_from_voltage_and_current(voltage=5, current=0.01)
ohms_law.calculate_current_from_power_and_resistance(power=2.4, resistance=33)

print(f"\nVoltage: {ohms_law.voltage}")
print(f"Power: {ohms_law.power}")
print(f"Resistance: {ohms_law.resistance}")
print(f"Current: {ohms_law.current}")