#KYRA CRAWFORD

import pygame, time, sys

pygame.init()
pygame.time.delay(100)

screen = pygame.display.set_mode((800,800))
white = [255,255,255]
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]

screen.fill(green)
pygame.display.set_caption('MY GAME')

pygame.display.flip()
pygame.time.delay(1000000)


run = True

while run:
    pygame.time.delay(1000)
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
pygame.quit()
