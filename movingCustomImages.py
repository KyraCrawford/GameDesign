# KYRA CRAWFORD
# TESTING custom backgrounds and custom sprites

import pygame
import time, sys

pygame.init()
screen = pygame.display.set_mode((640,480))
bg = pygame.image.load("marx.jpg")
god = pygame.image.load("wosh.jpg")
x = 20
y = 20

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
    if keyBoardKey[pygame.K_UP]: # subtract from y
        y -= speed
    if keyBoardKey[pygame.K_DOWN]: # add to y
        y += speed
    screen.blit(bg,(0,0))
    screen.blit(god,(x,y))
    pygame.display.update()
    pygame.time.delay(30)

pygame.quit()
