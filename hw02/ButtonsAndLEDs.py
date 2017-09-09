#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time

buttonL = "GP0_3"
buttonR = "GP0_4"
buttonD = "GP0_5"
buttonU = "GP0_6"


#Are these pins available for use like this on GPS?
LED1 = "GP1_3"
LED2 = "GP1_4"
LED3 = "GP1_5"
LED4 = "GP1_6"

#LED/output Setup
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)

#Button/input Setup
GPIO.setup(buttonL, GPIO.IN)
GPIO.setup(buttonR, GPIO.IN)
GPIO.setup(buttonD, GPIO.IN)
GPIO.setup(buttonU, GPIO.IN)

#To turn on the LEDs
GPIO.output(LED1, 1)
GPIO.output(LED2, 1)
GPIO.output(LED3, 1)
GPIO.output(LED4, 1)



#map buttons to LEDs
map = {buttonL: LED1, buttonR: LED2, buttonU: LED3, buttonD: LED4}

def updateLED(channel1):
     print("channel = " + channel)
     state = GPIO.input(channel)
     GPIO.output(map[channel], state)
     print(map[channel] + "Toggled")

print("Running...")

GPIO.add_event_detect(buttonL, GPIO.BOTH, callback = updateLED)
GPIO.add_event_detect(buttonR, GPIO.BOTH, callback = updateLED)
GPIO.add_event_detect(buttonD, GPIO.BOTH, callback = updateLED)
GPIO.add_event_detect(buttonU, GPIO.BOTH, callback = updateLED)

try:
     while True:
         time.sleep(100)


except KeyboardInterrupt:
     print("Cleaning Up")
     GPIO.cleanup()
