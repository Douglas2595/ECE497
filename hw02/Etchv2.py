#!/usr/bin/env python

import pygame, sys
from pygame.locals import *

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
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        if x < ((size-1)*100): x+=100
    if key[pygame.K_LEFT]:
        if x > 50: x-=100
    if key[pygame.K_UP]:
        if y > 50: y-=100
    if key[pygame.K_DOWN]:
        if y < ((size-1)*100): y+=100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            screen.fill((255,255,255))
