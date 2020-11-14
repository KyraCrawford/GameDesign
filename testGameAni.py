# KYRA CRAWFORD

import pygame, os, sys

pygame.init()

idle = ['fishingguy\idle1.png','fishingguy\idle2.png','fishingguy\idle3.png','fishingguy\idle4.png']
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH,HEIGHT))
bg = pygame.image.load('fishingguy\swamp.jpg')
counter = 0
counter = (counter + 1) % len(idle)
player = pygame.image.load(idle[counter])
playerX = 20
playerY = 20
jump = 3
Jump = False
def redrawScreen():
    screen.blit(bg,(0,0))
    screen.blit(player, (playerX, playerY))
    pygame.display.flip()
    pygame.time.delay(30)
def moveright():
    counter = 0
    speed = 1
    walkright = ['fishingguy\walk1.png','fishingguy\walk2.png','fishingguy\walk3.png','fishingguy\walk4.png','fishingguy\walk5.png']
    counter = (counter + 1) % len(walkright)
    player = pygame.image.load(walkright[counter])
    playerX = playerX + speed
def moveleft():
    counter = 0
    speed = 1
    walkleft = ['fishingguy\walkleft1.png','fishingguy\walkleft2.png','fishingguy\walkleft3.png','fishingguy\walkleft4.png','fishingguy\walkleft5.png']
    counter = (counter + 1) % len(walkleft)
    player = pygame.image.load(walkleft[counter])
    playerX = playerX - speed
def jumping():
    counter = 0
    speed = 1
    walk = ['fishingguy\walk1.png','fishingguy\walk2.png','fishingguy\walk3.png','fishingguy\walk4.png','fishingguy\walk5.png']
    jumppic = pygame.image.load('fishingguy\jump.png')
    if keyBoardKey[pygame.K_UP]: # subtract from y
        counter = (counter + 1) % len(walk)
        player = pygame.image.load(walk[counter])
        playerY -= speed
    if keyBoardKey[pygame.K_DOWN]: # add to y
        counter = (counter + 1) % len(walk)
        player = pygame.image.load(walk[counter])
        playerY += speed
    if keyBoardKey[pygame.K_SPACE]: #jumping
        Jump = True
        player = jumppic
run = True
while run:
    speed = 1
    counter = 0
    keyBoardKey = pygame.key.get_pressed()
    if keyBoardKey[pygame.K_RIGHT]:
        moveright()
    if keyBoardKey[pygame.K_LEFT]:
        moveleft()
    if not Jump: # this is for moving up and down without a jump
        jumping()
    else:
        if jump >= -10:
            playerY -= (jump*abs(jump))/2
            jump -= 1
        else:
            jump = 3
            Jump = False
            player = pygame.image.load(idle[counter])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    redrawScreen()
pygame.quit()
