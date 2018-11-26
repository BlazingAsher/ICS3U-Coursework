# Copyright (C) 2018 David Hui. All rights reserved.
# Permission is hereby granted to modify and redistribute this file for educational purposes with attribution.
from pygame import *
from math import pi

screen = display.set_mode((400, 500))
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

    screen.fill(GREEN)
    # draw.ellipse(screen, WHITE, (100, 100, 250, 200), 4)
    # draw.arc(screen, WHITE, (100, 100, 250, 200), 0, pi/2, 4)
    # draw.arc(screen, RED, (100, 100, 250, 200), pi/2, pi, 4)
    # draw.arc(screen, BLACK, (100, 100, 250, 200), pi, pi+pi/2, 4)
    # draw.arc(screen, BLUE, (100, 100, 250, 200), pi+pi/2, 2*pi, 4)
    draw.rect(screen, WHITE, (150,0,100,50), 2)
    draw.rect(screen, WHITE, (50,0,300,160), 2)
    draw.arc(screen, WHITE, (150,110,100,100), pi, 2*pi, 2)
    draw.arc(screen, WHITE, (100, 400, 200, 200), 0, pi, 2)
    draw.circle(screen, WHITE, (200, 140), 4)
    draw.circle(screen, WHITE, (0,0), 10, 2)
    draw.circle(screen, WHITE, (400, 0), 10, 2)


    display.flip()

raise SystemExit
