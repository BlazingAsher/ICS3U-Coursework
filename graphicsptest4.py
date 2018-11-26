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

running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    mp = mouse.get_pos()
    mb = mouse.get_pressed()

    if mb[0]:
        draw.line(screen, (randint(0,255), randint(0,255), randint(0,255)), mp, (mp[0]+randint(-20, 20), mp[1]+randint(-20,20)))
        display.flip()

raise SystemExit
