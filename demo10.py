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
    screen.fill(BLACK)
    mp = mouse.get_pos()
    # Draw the top
    for x in range(-20, 23, 3):
        draw.line(screen, GREEN, (mp[0]+x, mp[1]-20), (width//2+(20*x), 0))
        draw.line(screen, GREEN, (mp[0] + x, mp[1] + 20), (width//2 + (20 * x), height))
        draw.line(screen, GREEN, (mp[0] - 20, mp[1] +x), (0, height//2 + (20 * x)))
        draw.line(screen, GREEN, (mp[0] + 20, mp[1] + x), (width, height//2 + (20 * x)))
    display.flip()

raise SystemExit
