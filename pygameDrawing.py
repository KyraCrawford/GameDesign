#KYRA CRAWFORD

import pygame, time, sys

pygame.init()
pygame.time.delay(100)
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH,HEIGHT))
white = [255,255,255]
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]

screen.fill(green)
pygame.display.set_caption('MY SHAPES')
pygame.display.flip()
pygame.time.delay(100)

run = True
# variables to control the objects/shapes
x = 20
y = 20
rad = 30
hbox, wbox = 20, 20
rect = pygame.Rect(x, y, hbox, wbox)

while run:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
    # we are moving our rectangle around
    speed = 1
    keyBoardKey = pygame.key.get_pressed() # checking what key is pressed
    if keyBoardKey[pygame.K_LEFT]: # subtract from x
        rect.x -= speed
        rad -= speed
    if keyBoardKey[pygame.K_RIGHT]: # add to x
        rect.x += speed
        rad += speed
    if keyBoardKey[pygame.K_UP]: # subtract from y
        rect.y -= speed
    if keyBoardKey[pygame.K_DOWN]: # add to y
        rect.y += speed
# setting boundaries for the movement of shapes
    if rect.x < 0 : rect.x = 0 # left boundary
    if rect.x > WIDTH-hbox : rect.x = WIDTH - hbox # right boundary
    if rect.y < 0 : rect.y = 0 # top boundary
    if rect.y > HEIGHT - hbox : rect.y = HEIGHT - wbox # bottom boundary
    if rad < y : rad = y
    if rad < 0 : rad = 0 # left boundary (follow rules of rect)
    if rad > WIDTH-x : rad = WIDTH -x # right boundary (follow rule of rect)

    screen.fill(green)
    pygame.draw.circle(screen,(blue),(x+300,y+220),rad, 2)
    pygame.draw.rect(screen,(red),rect)
    pygame.display.update()

pygame.quit()

# check for out of window
