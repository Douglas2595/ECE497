#!/usr/bin/env python3
#Douglas Wise
#Sep 18, 2017

import Adafruit_BBIO.GPIO as GPIO
import time
import smbus

#button assignments
buttonL = "GP0_3"
buttonR = "GP0_4"
buttonD = "GP0_5"
buttonU = "GP0_6"

#Button/input Setup
GPIO.setup(buttonL, GPIO.IN)
GPIO.setup(buttonR, GPIO.IN)
GPIO.setup(buttonD, GPIO.IN)
GPIO.setup(buttonU, GPIO.IN)

bus = smbus.SMBus(1)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

delay = 1; # Delay between images in s

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

game = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
]

x = 0x01
y = 0

while 1:
    clock.tick(15)
    if GPIO.input(buttonR):
        if x > 0x01: x >> 1
    if not GPIO.input(buttonL):
        if x < 0x80: x << 1
    if GPIO.input(buttonU):
        if y < 15: y += 2
    if not GPIO.input(buttonD):
        if y > 0: y -= 2

    game[y] = game[y] | x
    print('y = {}, x = {}'.format(y, format(x, '02x'))
    bus.write_i2c_block_data(matrix, 0, game)
