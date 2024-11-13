import machine

class Button:
    def __init__(self, pin, callback):
        self.button = machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP)
        self.button.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback)
