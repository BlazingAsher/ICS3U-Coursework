# Copyright (C) 2018 David Hui. All rights reserved.
# Permission is hereby granted to modify and redistribute this file for educational purposes with attribution.
from pygame import *

size = width, height = 800, 400
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

    for i in range(20, width, 20):
        draw.line(screen, GREEN, (i, 0), (i, height))
    for i in range(20, height, 20):
        draw.line(screen, GREEN, (0, i), (width, i))
    display.flip()

raise SystemExit
