#!/usr/bin/env python 3
#read a tmp101
#sudo apt install python3-smbus

import smbus
import time

bus = smbus.SMBus(1)
address = 0x48

while True:
    temp = bus.read_byte_data(address, 0)
    temp1 = temp*1.8 + 32
    print(temp1, end="\r")
    time.sleep(0.25)
