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

smile = [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
]
# # The first byte is GREEN, the second is RED.
# smile = [0x00, 0x3c, 0x00, 0x42, 0x28, 0x89, 0x04, 0x85,
#     0x04, 0x85, 0x28, 0x89, 0x00, 0x42, 0x00, 0x3c
# ]
# frown = [0x3c, 0x00, 0x42, 0x00, 0x85, 0x20, 0x89, 0x00,
#     0x89, 0x00, 0x85, 0x20, 0x42, 0x00, 0x3c, 0x00
# ]
# neutral = [0x3c, 0x3c, 0x42, 0x42, 0xa9, 0xa9, 0x89, 0x89,
#     0x89, 0x89, 0xa9, 0xa9, 0x42, 0x42, 0x3c, 0x3c
# ]

# bus.write_i2c_block_data(matrix, 0, frown)
# for fade in range(0xef, 0xe0, -1):
#     bus.write_byte_data(matrix, fade, 0)
#     time.sleep(delay/10)

# bus.write_i2c_block_data(matrix, 0, neutral)
# for fade in range(0xe0, 0xef, 1):
#     bus.write_byte_data(matrix, fade, 0)
#     time.sleep(delay/10)

bus.write_i2c_block_data(matrix, 0, smile)
