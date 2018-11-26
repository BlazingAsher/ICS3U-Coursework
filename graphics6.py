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
    for i in range(20,width,40):
        for j in range(20, height, 40):
            draw.circle(screen, (randint(0, 255), randint(0, 255), randint(0, 255)), (i, j), 18, 2)
            time.wait(10)
            display.flip()

raise SystemExit
