#!/usr/bin/env python2

import Adafruit_BBIO.GPIO as GPIO
import time
import pygame, sys
from pygame.locals import *

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

pygame.init()

size = input('Game Size: ')

screen = pygame.display.set_mode((size*100,size*100))

x=10
y=10
xgrid = 0
ygrid = 0

clock = pygame.time.Clock()
screen.fill((255,255,255))

while 1:
    clock.tick(15)
    Rect = pygame.Rect(x, y, 80, 80)
    pygame.draw.rect(screen, (0,0,0), Rect)
    for i in range(size-1):
        pygame.draw.line(screen, (0,0,0), (xgrid, ygrid+(i*100)+100), (xgrid+(size*100), ygrid+(i*100)+100))
        pygame.draw.line(screen, (0,0,0), (xgrid+100+(i*100), ygrid), (xgrid+100+(i*100), ygrid+(size*100)))
    pygame.display.update()

    def update(channel):
         if GPIO.input(buttonR):
             if x < ((size-1)*100): x+=100
         if GPIO.input(buttonL):
             if x > 50: x-=100
         if GPIO.input(buttonU):
             if y > 50: y-=100
         if GPIO.input(buttonU):
             if y < ((size-1)*100): y+=100

    GPIO.add_event_detect(buttonL, GPIO.FALLING, callback = update)
    GPIO.add_event_detect(buttonR, GPIO.FALLING, callback = update)
    GPIO.add_event_detect(buttonD, GPIO.FALLING, callback = update)
    GPIO.add_event_detect(buttonU, GPIO.FALLING, callback = update)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            screen.fill((255,255,255))
