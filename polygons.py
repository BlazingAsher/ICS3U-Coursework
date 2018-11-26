# Copyright (C) 2018 David Hui. All rights reserved.
# Permission is hereby granted to modify and redistribute this file for educational purposes with attribution.
from pygame import *

screen = display.set_mode((800, 600))
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
    screen.fill(WHITE)
    draw.circle(screen, RED, (400, 300), 50)
    draw.polygon(screen, GREEN, [(400, 500), (500, 500), (450, 300)])
    draw.polygon(screen, RED, [(100, 100), (150, 50), (200, 100), (150, 150)], 5)

    # A house
    draw.rect(screen, GREEN, Rect(300,300,100,70))
    # The roof
    draw.polygon(screen, GREEN, [(300,300),(400,300),(350,275)])
    # The window
    draw.rect(screen, WHITE, Rect(315,315,20,20))
    # The door
    draw.rect(screen, WHITE, Rect(355, 330, 25, 40))
    display.flip()

raise SystemExit

