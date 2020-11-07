# KYRA CRAWFORD

import pygame

# drawing with pygame
# HW: ask user for a color, create window with that color, ask width and height of

pygame.init() # always first command with pygame
colors = {'black':(0,0,0), 'red':(255,0,0), 'green':(0,255,0), 'blue':(0,0,255), 'white':(255,255,255)}

height = input('What is the height of your window? (10-1000) ')
width = input('What is the width of your window? (10-1000) ')
color = input('What color do you want to fill the window? (red/green/blue/black/white) ')

height = int(height)
width = int(width)

color = colors.get(str(color))

window = pygame.display.set_mode((height,width))
window.fill(color)

pygame.display.set_caption('YOUR WINDOW')
pygame.display.flip() # updates the display (can also use display.update)

run = True

while run:
    pygame.time.delay(1000)
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
pygame.quit()
