#!/usr/bin/env python 3
#read a tmp101
#sudo apt install python3-smbus

import Adafruit_BBIO.GPIO as GPIO
import smbus
import time

alert1 = "GPIO_3"
alert2 = "GPIO_5"

GPIO.setup(alert1, GPIO.IN)
GPIO.setup(alert2, GPIO.IN)

bus = smbus.SMBus(1)
address1 = 0x48
address2 = 0x49

map1 = {alert1: address1, alert2: address2}
map2 = {alert1: 'temp1', alert2: 'temp2'}

def alert(channel):
    temp = bus.read_byte_data(map1[channel], 0)
    print("Alert: " + map2[channel] + " " + temp)

GPIO.add_event_detect(alert1, GPIO.BOTH, callback = alert)
GPIO.add_event_detect(alert1, GPIO.BOTH, callback = alert)

while True:

    temp1 = bus.read_byte_data(address1, 0)
    temp2 = bus.read_byte_data(address2, 0)

    temp1 = temp1*1.8 + 32
    temp2 = temp2*1.8 + 32

    print(temp1, temp2, end="\r")
    time.sleep(0.25)
