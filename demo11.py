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
seed = -10
increase = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    screen.fill(BLACK)

    for y in range(50, height-50, 20):
        i = 0
        lastpt = (0,y)
        for x in range(0, width+10, 10):
            if i%2 == 0:
                draw.line(screen, GREEN, lastpt, (x, y+seed))
                lastpt = (x, y+seed)
            else:
                draw.line(screen, GREEN, lastpt, (x,y))
                lastpt = (x, y)
            i+=1
    if increase:
        seed+=1
        print(seed)
        if seed == 10:
            increase = False
    else:
        seed-=1
        if seed == -10:
            increase = True
    clock = time.Clock()
    clock.tick(10)
    display.flip()

raise SystemExit
