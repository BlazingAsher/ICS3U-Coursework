#bouncingDemo1.py
from pygame import *
from random import *
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
        
box=Rect(200,100,50,50)
print(box.left,box.top,box.right,box.bottom)
myClock=time.Clock()

vx = 5
vy = 5

colours = []

while len(colours) < 100:
    colours.append
changeCount = 3
timeout = 30
running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False

    screen.fill(BLACK)
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
    print(colours)
    draw.rect(screen, colours[0], box)
    box.left += vx
    box.top += vy

    if box.right == width or box.left == 0:
        vx = -vx
    if box.bottom == height or box.top == 0:
        vy = -vy

    if mb[0] and timeout < 1:
        changeCount -= 1
        if changeCount == 0:
            del colours[0]
            if len(colours) == 0:
                raise SystemExit
            changeCount = 3
            box.width = 50
            box.height = 50
        timeout = 30

    if box.collidepoint(mx, my) and mb[0]:
        box.left = randint(100, 700)
        box.top = randint(100, 500)
        if box.width > 30:
            box.width -= 5
            box.height -= 5
        else:
            print("Game over!")
            raise SystemExit

    timeout-=1
    myClock.tick(60)
    display.flip() 
raise SystemExit






