#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time

button="PAUSE"
LED="USR3"

# Set the GPIO pins:
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

while True:
    state = GPIO.input(button)
    GPIO.output(LED, state)

    GPIO.wait_for_edge(button, GPIO.BOTH)
    print("Pressed")
