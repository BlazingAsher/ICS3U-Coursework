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
    if mb[0]:
        draw.polygon(screen, GREEN, [(mp[0], mp[1]-size), (mp[0]+size, mp[1]), (mp[0], mp[1]+size), (mp[0]-size, mp[1])], 1)
    if mb[2]:
        screen.fill(BLACK)
    display.flip()

raise SystemExit
