# Copyright (C) 2018 David Hui. All rights reserved.
# Permission is hereby granted to modify and redistribute this file for educational purposes with attribution.
# USE THIS FOR THE BRUSH AND ERASER TOOL
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
    mp = mouse.get_pos()
    mb = mouse.get_pressed()

    center = (width//2, height//2)
    screen.fill(BLACK)
    #print(center)
    if mb[2]:
        dx = mp[0]-center[0]
        dy = mp[1]-center[1]

        dist = (dy**2 + dx**2)**(1/2)

        draw.circle(screen, RED, center, 10)
        draw.circle(screen, RED, mp, 10)
        for d in range(20, int(dist), 20):
            dot = (int(center[0]+dx*d/dist), int(center[1]+dy*d/dist))
            print(dot)
            draw.circle(screen, GREEN, dot, 5)
            print(d)
    display.flip()

raise SystemExit
