# Copyright (C) 2018 David Hui. All rights reserved.
# Permission is hereby granted to modify and redistribute this file for educational purposes with attribution.
from pygame import *
from random import randint

size = width, height = 600, 600
screen = display.set_mode(size)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

running = True
clock = time.Clock()
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False

    for x in range(0,width,width//20):
        for y in range(0,height,height//20):
            draw.rect(screen, (randint(0,255), randint(0,255), randint(0,255)), (x,y,width//20,height//20))

    draw.rect(screen, WHITE, (0,(height//20)*randint(0,19), width, height//20))

    clock.tick(2)
    display.flip()

raise SystemExit
