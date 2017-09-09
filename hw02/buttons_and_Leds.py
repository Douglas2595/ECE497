#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time
buttonP = "PAUSE"
buttonM = "MODE"
Ledp = "RED"
Ledm = "GREEN"

# set pins
GPIO.setup(Ledp,    GPIO.OUT)
GPIO.setup(Ledm,    GPIO.OUT)
GPIO.setup(buttonP, GPIO.IN)
GPIO.setup(buttonM, GPIO.IN)

GPIO.output(LEDp, 1)
GPIO.output(LEDm, 1)

print("Running...")

GPIO.add.event_detect(buttonP, GPIO.BOTH)
GPIO.add.event_detect(buttonM, GPIO.BOTH)

while True:
    if GPIO.event_detected(buttonP):
        state = GPIO.input(buttonP)
        GPIO.output(LEDp, state)
        print(LEDp + "Toggled")

    if GPIO.event_detected(buttonM):
        state = GPIO.input(buttonM)
        GPIO.output(LEDm, state)
        print(LEDm + "Toggled")
