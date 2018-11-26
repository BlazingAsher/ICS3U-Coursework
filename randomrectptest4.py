# Copyright (C) 2018 David Hui. All rights reserved.
# Permission is hereby granted to modify and redistribute this file for educational purposes with attribution.
from pygame import *
from random import randint

size = width, height = 800, 600
screen = display.set_mode(size)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

rectList = [Rect(randint(0, width-40), randint(0, height-40), 40, 40) for i in range(10)]

running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    mp = mouse.get_pos()
    mb = mouse.get_pressed()
    for rect in rectList:
        color = GREEN
        if rect.collidepoint(mp):
            if mb[0]:
                color = RED
            else:
                color = BLUE
        draw.rect(screen, color, rect)
    display.flip()

raise SystemExit
