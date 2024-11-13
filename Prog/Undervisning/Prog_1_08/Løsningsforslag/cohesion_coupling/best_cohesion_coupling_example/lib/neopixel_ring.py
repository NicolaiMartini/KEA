import neopixel
import machine

class NeoPixelRing:
    def __init__(self, pin, num_pixels):
        self.np = neopixel.NeoPixel(machine.Pin(pin), num_pixels)
        self.num_pixels = num_pixels

    def set_color(self, color):
        for i in range(self.num_pixels):
            self.np[i] = color
        self.np.write()