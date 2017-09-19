#!/usr/bin/env python 3
#Douglas Wise
#read a tmp101
#sudo apt install python3-smbus

import Adafruit_BBIO.GPIO as GPIO
import smbus
import time
import subprocess

alert1 = "GP0_3"
alert2 = "GP0_5"

GPIO.setup(alert1, GPIO.IN)
GPIO.setup(alert2, GPIO.IN)

bus = smbus.SMBus(1)
address1 = 0x48
address2 = 0x49

bus.write_byte_data(address1, 3, 24)

# subprocess.run('i2cset', '-y', '0x48', '11', '24', 'w')
# subprocess.run('i2cset', '-y', '0x49', '11', '24', 'w')

map1 = {alert1: address1, alert2: address2}
map2 = {alert1: 'temp1', alert2: 'temp2'}

def alert(channel):
    temp = bus.read_byte_data(map1[channel], 0)
    print("Alert: {} is {}".format(map2[channel], temp), end="\r")

GPIO.add_event_detect(alert1, GPIO.BOTH, callback = alert)
GPIO.add_event_detect(alert2, GPIO.BOTH, callback = alert)

while 1:

    temp1 = bus.read_byte_data(address1, 0)
    temp2 = bus.read_byte_data(address2, 0)

    temp1 = temp1*1.8 + 32
    temp2 = temp2*1.8 + 32

    print(temp1, temp2, end="\r")
    time.sleep(0.25)
