# KYRA CRAWFORD
# TESTING custom backgrounds and custom sprites

import pygame
import time, sys

pygame.init()
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH,HEIGHT))
bg = pygame.image.load("marx.jpg")
god = pygame.image.load("wosh.jpg")
x = 20
y = 20
hbox, wbox = 20, 20
jump = 10
Jump = False
def redrawScreen():
    screen.blit(bg,(0,0))
    screen.blit(god,(x,y))
    pygame.display.update()
    pygame.time.delay(30)
run = True
while run:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
    speed = 2
    keyBoardKey = pygame.key.get_pressed() # checking what key is pressed
    if keyBoardKey[pygame.K_LEFT]: # subtract from x
        x -= speed
    if keyBoardKey[pygame.K_RIGHT]: # add to x
        x += speed
    if not Jump: # this is for moving up and down without a jump
        if keyBoardKey[pygame.K_UP]: # subtract from y
            y -= speed
        if keyBoardKey[pygame.K_DOWN]: # add to y
            y += speed
        if keyBoardKey[pygame.K_SPACE]: #jumping
            Jump = True
    else:
        if jump >= -10:
            y -= (jump*abs(jump))/2
            jump -= 1
        else:
            jump = 10
            Jump = False
    if x < 0 : x = 0 # left boundary
    if x > WIDTH-hbox : x = WIDTH - hbox # right boundary
    if y < 0 : y = 0 # top boundary
    if y > HEIGHT - hbox : y = HEIGHT - wbox # bottom boundary
    redrawScreen()
pygame.quit()
