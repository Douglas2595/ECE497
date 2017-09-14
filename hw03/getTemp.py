#!/usr/bin/env python 3
#read a tmp101
#sudo apt install python3-smbus

import smbus
import time

bus = smbus.SMBus(1)
address = 0x48

while True:
    temp = bus.read_byte_data(address, 0)
    print(temp, end="\r")
    time.sleep(0.25)
    
