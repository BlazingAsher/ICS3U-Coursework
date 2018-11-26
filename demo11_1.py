# Copyright (C) 2018 David Hui. All rights reserved.
# Permission is hereby granted to modify and redistribute this file for educational purposes with attribution.
from pygame import *

size = width, height = 800, 600
screen = display.set_mode(size)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

running = True
decrease = True
blueVal = 250
adder = -5
tickClock = time.Clock()

while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False

    for x in range(80, 720, 20):
        draw.rect(screen, GREEN, (x, 80, 20, 20), 2)
        draw.rect(screen, GREEN, (x, 500, 20, 20), 2)
    for y in range(100, 500, 20):
        draw.rect(screen, GREEN, (80, y, 20, 20), 2)
        draw.rect(screen, GREEN, (700, y, 20, 20), 2)
    draw.rect(screen, (0, 0, blueVal), (100, 100, 600, 400))

    if blueVal == 255 or blueVal == 0:
        adder = -adder
    blueVal+=adder

    tickClock.tick(120)

    display.flip()

raise SystemExit
