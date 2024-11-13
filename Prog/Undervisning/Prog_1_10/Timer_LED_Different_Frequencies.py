from machine import Pin, Timer
from time import sleep

# LEDs
red_led_pin=12
red_led=Pin(red_led_pin,Pin.OUT)
yellow_led_pin=13
yellow_led=Pin(yellow_led_pin,Pin.OUT)

# Callback function for the red timer
def toggle_red_led(timer):
	red_led.value(not red_led.value()) # Toggle LED state (ON/OFF)
	print(f"Red LED is: {red_led.value()}")

# Callback function for the yellow timer
def toggle_yellow_led(timer):
	yellow_led.value(not yellow_led.value()) # Toggle LED state (ON/OFF)
	print(f"Yellow LED is: {yellow_led.value()}")

# Create periodic timers
red_timer=Timer(1)
yellow_timer=Timer(2)

# Init the timers
red_timer.init(mode=Timer.PERIODIC,period=500,callback=toggle_red_led) # Timer repeats every 0.5 seconds
yellow_timer.init(mode=Timer.PERIODIC,period=2000,callback=toggle_yellow_led) # Timer repeats every 2 seconds

try:
	# Main loop(optional)
	while True:
		print("Main loop is running")
		sleep(2)
except KeyboardInterrupt:
	# Keyboard Interrupt occurred, deinitialize the timers
	red_timer.deinit()
	yellow_timer.deinit()
	print("Timers deinitialized")
	# Turn off the LEDs
	yellow_led.value(0)
	red_led.value(0)