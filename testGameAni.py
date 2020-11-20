# KYRA CRAWFORD
import pygame
pygame.init()
WIDTH = 1000
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('axeguy\walk1.png'), pygame.image.load('axeguy\walk2.png'), pygame.image.load('axeguy\walk3.png'), pygame.image.load('axeguy\walk4.png'), pygame.image.load('axeguy\walk5.png'), pygame.image.load('axeguy\walk6.png'), pygame.image.load('axeguy\walk5.png'), pygame.image.load('axeguy\walk4.png'), pygame.image.load('axeguy\walk3.png'), pygame.image.load('axeguy\walk2.png'), pygame.image.load('axeguy\walk1.png')]
walkLeft = [pygame.image.load('axeguy\walkleft1.png'), pygame.image.load('axeguy\walkleft2.png'), pygame.image.load('axeguy\walkleft3.png'), pygame.image.load('axeguy\walkleft4.png'), pygame.image.load('axeguy\walkleft5.png'), pygame.image.load('axeguy\walkleft4.png'), pygame.image.load('axeguy\walkleft5.png'), pygame.image.load('axeguy\walkleft6.png'), pygame.image.load('axeguy\walkleft5.png'), pygame.image.load('axeguy\walkleft4.png'), pygame.image.load('axeguy\walkleft3.png'), pygame.image.load('axeguy\walkleft2.png'), pygame.image.load('axeguy\walkleft1.png')]
bg1 = pygame.image.load('axeguy\wallbg.jpg')
bg2 = pygame.image.load('axeguy\crystalsbg.jpg')
bg3 = pygame.image.load('axeguy\cavebg.png')
bg4 = pygame.image.load('axeguy\caveexit.png')
character = pygame.image.load('axeguy\idle2.png')
back = ()
back = bg1
x = 0
y = 400
width = 40
height = 60
speed = 5
#to control the frames
clock = pygame.time.Clock()
Jump = False
high = 8
#control left and right move
left = False
right = False
#control my list
walkCount = 0
def changebg():
    global back
    global bg2, bg3, bg4
    if back == bg1:
        back = bg2
        x = 0
    elif back == bg2:
        back = bg3
        x = 0
    elif back == bg3:
        back = bg4
        x=0
    else:
        pygame.quit()
    screen.blit(back,(0,0))
def redrawGameWindow():
    global walkCount #it makes sure is using the global walkCount that created earlier
    screen.blit(back, (0,0))
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    elif x == 1000:
        changebg()
    else:
        screen.blit(character, (x, y))
        walkCount = 0
    pygame.display.update()
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < WIDTH - speed - width:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        walkCount = 0
    if not Jump:
        if keys[pygame.K_SPACE]:
            Jump = True
            left = False
            right = False
            walkCount = 0
    else:
        if high >= -8:
            y -= (high * abs(high)) * 0.5
            high -= 1
        else:
            high = 8
            Jump = False

    redrawGameWindow()
pygame.quit()
