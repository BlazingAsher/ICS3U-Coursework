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

dots = [(randint(0, width), randint(0, height)) for i in range(100)]
clock = time.Clock()

while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    screen.fill(BLACK)
    for i in range(len(dots)):
        draw.circle(screen, WHITE, dots[i], 3)
        dots[i] = (dots[i][0], dots[i][1]+4) if dots[i][1] < height else (dots[i][0], 0)
    clock.tick(30)
    display.flip()

raise SystemExit
