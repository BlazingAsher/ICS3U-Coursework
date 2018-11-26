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

size = 40

running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    mp = mouse.get_pos()
    mb = mouse.get_pressed()
    smallest = 10000

    for x in range(40, width - 50, 80):
        y = height//2-20
        length = ((mp[0]-x-35)**2 + (mp[1]-y-20)**2)**(1/2)
        if length < smallest:
            smallest = length

    i = 0
    for x in range(40, width-50, 80):

        y = height // 2 - 20
        length = ((mp[0] - x-35) ** 2 + (mp[1] - y-20) ** 2) ** (1 / 2)

        if length == smallest:
            color = (70+i*20, 0, 0)
        else:
            color = (0, 70+i*20, 0)
        draw.rect(screen, color, (x, height//2-20, 70, 20))
        i+=1
    display.flip()

raise SystemExit
