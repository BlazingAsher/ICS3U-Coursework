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
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    x = 10
    y = 300
    h = 20
    v = 5
    while x<800:
        draw.line(screen, GREEN, (x,y), (x, y+v))
        y+=v
        draw.line(screen, GREEN, (x,y), (x+h,y))
        x+=h
        v+=10
        draw.line(screen, GREEN, (x,y), (x, y-v))
        y-=v
        draw.line(screen, GREEN, (x,y), (x+h, y))
        x+=h
        v+=10
    display.flip()

raise SystemExit
