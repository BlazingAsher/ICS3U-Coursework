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
    mb = mouse.get_pressed()
    if mb[2]:
        center = (width//2, height//2)
        mp = mouse.get_pos()
        distMToC = ((mp[0]-center[0])**2 + (mp[1]-center[1])**2)**(1/2)
        circleR = distMToC//4
        screen.copy()
        draw.circle(screen, (randint(0,255), randint(0,255), randint(0,255)), mp, int(circleR))
    elif mb[0]:
        screen.fill(BLACK)
    display.flip()

raise SystemExit
