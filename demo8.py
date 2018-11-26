# Copyright (C) 2018 David Hui. All rights reserved.
# Permission is hereby granted to modify and redistribute this file for educational purposes with attribution.

# Nice part of paint program
# Drag and drop
from pygame import *

size = width, height = 800, 600
screen = display.set_mode(size)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

mMode = "up"

running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    mb = mouse.get_pressed()
    mp = mx, my = mouse.get_pos()

    if mMode == "up" and mb[0]:
        mMode = "down"
        screenShot = screen.copy()
        mouse.set_visible(False)
        print("hello")

    if mMode == "down" and not mb[0]:
        mMode = "up"
        mouse.set_visible(True)
        print("bye")

    if mb[0]:
        screen.blit(screenShot, (0, 0))
        draw.circle(screen, RED, mp, 25)
    display.flip()

raise SystemExit
