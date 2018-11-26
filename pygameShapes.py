# Copyright (C) 2018 David Hui. All rights reserved.
# Permission is hereby granted to modify and redistribute this file for educational purposes with attribution.
from pygame import *

screen = display.set_mode((900, 600))
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
    draw.line(screen,BLACK,(0,300),(900,300))
    draw.line(screen, BLACK, (300,0), (300, 600))
    draw.line(screen, BLACK, (600, 0), (600, 600))

    # Plus
    draw.line(screen, BLACK, (50,150), (250, 150))
    draw.line(screen, BLACK, (150, 50), (150, 250))

    # X
    draw.line(screen, BLACK, (350, 50), (550, 250))
    draw.line(screen, BLACK, (350, 250), (550, 50))

    # Circle
    draw.circle(screen, GREEN, (750,150), 130)

    # Square
    draw.rect(screen, RED, Rect(50,350, 200, 200))

    # Triangle
    draw.polygon(screen, BLUE, [(350,550),(550,550),(450,350)])

    # Diamond
    draw.polygon(screen, (255,255,0), [(650,450),(750, 350), (850,450),(750, 550)])
    display.flip()

raise SystemExit
