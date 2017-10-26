#!/usr/bin/env python3
#Douglas Wise
import Adafruit_BBIO.GPIO as GPIO
import time

GP_in = "GP1_3"         # input gpio
GP_out = "GP1_4"        # output gpio

# set pins
GPIO.setup(GP_in,    GPIO.IN)
GPIO.setup(GP_out,    GPIO.OUT)

# initial out is off
GPIO.output(GP_out, 0)

# map input to output
map = {GP_in: GP_out}

# output function
def output(channel):
    print("channel =" + channel)
    state = GPIO.input(channel)         # get input value
    GPIO.output(map[channel], state)    # outputs input value

print("Running...")

# detects input calls output function
GPIO.add_event_detect(GP_in, GPIO.BOTH, callback=output)

try:
    while True:
        time.sleep(100)

except KeyboardInterrupt:
    print("Cleaning Up")
    GPIO.cleanup()
GPIO.cleanup()
