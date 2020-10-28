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
