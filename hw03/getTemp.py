#!/usr/bin/env python 3
#read a tmp101
#sudo apt install python3-smbus

import smbus
import time

bus = smbus.SMBus(1)
address1 = 0x48
address2 = 0x49

while True:
    temp1 = bus.read_byte_data(address1, 0)
    temp2 = bus.read_byte_data(address2, 0)
    temp1 = temp1*1.8 + 32
    temp2 = temp2*1.8 + 32
    print(temp1, end="\r")
    print(temp2, end="\r")
    time.sleep(0.25)
