# simple code to test if your devboard is even working at all
# blinks the onboard gpio25 led
# circuitpython

import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP25)  # GPIO25
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = not led.value  # toggle
    time.sleep(0.5)
