#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time
buttonP = "PAUSE"
buttonM = "MODE"
LEDp = "RED"
LEDm = "GREEN"

# set pins
GPIO.setup(LEDp,    GPIO.OUT)
GPIO.setup(LEDm,    GPIO.OUT)
GPIO.setup(buttonP, GPIO.IN)
GPIO.setup(buttonM, GPIO.IN)

GPIO.output(LEDp, 1)
GPIO.output(LEDm, 1)

map = {buttonP: LEDp, buttonM: LEDm}

def updateLED(channel):
    print("channel =" + channel)
    state = GPIO.input(channel)
    GPIO.output(map[channel], state)
    print(map[channel] + " Toggeled")

print("Running...")

GPIO.add.event_detect(buttonP, GPIO.BOTH, callback=updateLED)
GPIO.add.event_detect(buttonM, GPIO.BOTH, callback=updateLED)
try:
    while True:
        time.sleep(100)

except KeyboardInterrupt:
    print("Cleaning Up")
    GPIO.cleanup()
GPIO.cleanup()

