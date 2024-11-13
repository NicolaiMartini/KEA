import machine

class Potentiometer:
    def __init__(self, pin):
        self.adc = machine.ADC(machine.Pin(pin))
        self.adc.atten(machine.ADC.ATTN_11DB)
        self.adc.width(machine.ADC.WIDTH_10BIT)

    def read_value(self):
        return self.adc.read()