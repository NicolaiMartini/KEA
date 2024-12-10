# A simple LED and PWM demo program
from machine import Pin, PWM, ADC
import hw
from time import sleep
from portExp_MCP23S08 import PortExp_MCP23S08

# CONFIGURATION
# Hardware
pin_led_red = 26 # Red LED pin (must be a PWM able pin!)
pin_led_green = 2
pin_led_blue = 3


# Red LED
led_red_freq = 40 # The Red LED PWM frequency
led_red_duty = 256 # The Red LED duty cycle, 0-1023, e.g. 50% -> 512
led_red = PWM(Pin(pin_led_red), duty=0) # Create PWM object for the pin
# Green LED
led_green_freq=40
led_green_duty=512
led_green = PWM(Pin(pin_led_green), duty=0)
# Blue LED
led_blue_freq=40
led_blue_duty=758
led_blue=PWM(Pin(pin_led_blue), duty=0)
# Potentiometer, reading from 0 to 1023
potmeter_adc=ADC(Pin(hw.pin_potmeter))
potmeter_adc.atten(ADC.ATTN_11DB)
potmeter_adc.width(ADC.WIDTH_10BIT)

# Program
print("LED PWM test program")
while True:
    led_red.freq(potmeter_adc.read()+1)
    led_red.duty(potmeter_adc.read()) # Set the duty cycle

    led_green.freq(potmeter_adc.read()+1)
    led_green.duty(potmeter_adc.read())

    led_blue.freq(potmeter_adc.read()+1)
    led_blue.duty(potmeter_adc.read())
    sleep(0.01)
    