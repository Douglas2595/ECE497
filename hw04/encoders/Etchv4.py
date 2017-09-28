#!/usr/bin/env python3
#Douglas Wise
#Sep 18, 2017

import Adafruit_BBIO.GPIO as GPIO
import time
import smbus
import rcpy
import rcpy.encoder as encoder

#button assignments
clear = "PAUSE"

#Button/input Setup
rcpy.set_state(rcpy.RUNNING)
GPIO.setup(clear, GPIO.IN)

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
    e1_base = encoder.get(1) # read the encoders
    e2_base = encoder.get(2)

    if encoder.get(1) > e1_base:
        if x > 0x01: x = x >> 1
    if encoder.get(1) < e1_base:
        if x < 0x80: x = x << 1
    if encoder.get(2) < e2_base:
        if y < 14: y += 2
    if encoder.get(2) > e2_base:
        if y > 0: y -= 2
    if not GPIO.input(clear):
        game = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
        ]

    game[y] = game[y] | x

    bus.write_i2c_block_data(matrix, 0, game)

    time.sleep(delay/10)
