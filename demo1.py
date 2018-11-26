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
    mb = mouse.get_pressed() # (0,0,0) <- represents the position that is clicked eg. right is (0,0,1)
    mp = mouse.get_pos() # (x,y)

    if mb[2]:
        print("Right click!")
        for i in range(-20, 30, 10):
            draw.circle(screen, GREEN, (mp[0]+i,mp[1]), 5)
    elif mb[0]:
        screen.fill(BLACK)
    print(mp)
    display.flip()

raise SystemExit
