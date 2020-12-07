import pygame
import math
import random
import random, time, os, sys
import datetime

# setup display
pygame.init()
WIDTH, HEIGHT = 800, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")
# name= input('What is your name: ')
# setup  button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# set up fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)
INS_FONT = pygame.font.SysFont('comicsans', 25)

# load images.
images = []
for i in range(7):
    image = pygame.image.load("ImagesHM\hangman" + str(i) + ".png") # BUILDING OUR HANGING MAN
    images.append(image)

# game variables
hangman_status = 0
score = 0
FRUITS = ['STRAWBERRY','BLUEBERRY','APPLE','ORANGE','PEAR','PEACH','GRAPE'] #LEVEL OF WORDS
GADGETS = ['COMPUTER','MOUSE','KEYBOARD','HEADPHONES','MONITOR','LAPTOP','PHONE'] #LEVEL OF WORDS
CLOTHING = ['SHOES','SHIRT','SOCKS','PANTS','JACKET','BELT','SHORTS','HAT']
guessed = []
words = GADGETS
word = random.choice(words)
keyBoardKey = pygame.key.get_pressed()
# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
PURP = (114, 40, 189)

def INS():
    global keyBoardKey
    win.fill(WHITE)
    pygame.display.update()
    in1 = INS_FONT.render('HOW TO PLAY:',1, BLACK)
    in2 = INS_FONT.render('Guess the letters in the word',1, BLACK)
    in3 = INS_FONT.render('Once the man is completed, the game is over',1, BLACK)
    in4 = INS_FONT.render("Score will be kept in the document named,'SCORE_RECORDS_HM'" ,1, BLACK)
    in5 = INS_FONT.render('***THE LOWER THE SCORE, THE BETTER***',1, BLACK)
    next = INS_FONT.render('- PRESS SPACE TO CONTINUE -',1,BLACK)
    win.blit(in1,(WIDTH/2 - in1.get_width()/2,200))
    win.blit(in2,(WIDTH/2 - in2.get_width()/2,230))
    win.blit(in3,(WIDTH/2 - in3.get_width()/2,260))
    win.blit(in4,(WIDTH/2 - in4.get_width()/2,290))
    win.blit(in5,(WIDTH/2 - in5.get_width()/2,320))
    # win.blit(next,(WIDTH/2 - next.get_width()/2,550))
    pygame.display.update()
    pygame.time.delay(300)
    MENU()
    if keyBoardKey[pygame.K_SPACE]:
        print('SPACE PRESSED')
    pygame.display.update()
def SCORE(score):
    date = datetime.datetime.now()
    with open('SCORE_RECORDS_HM.txt') as s:
        records = open('SCORE_RECORDS_HM.txt','a')
        # records.write(str(name))
        # records.write(' - ')
        records.write(str(score))
        records.write(' wrong letters ')
        records.write(date.strftime('%Y/%m/%d %H:%M'))
        records.write('\n')
        records.close()
def MENU():
    global words
    global FRUITS, GADGETS, CLOTHING
    win.fill(WHITE)
    pygame.display.update()
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    button1 = WORD_FONT.render("[1] FRUITS",1, PURP)
    button2 = WORD_FONT.render('[2] GADGETS',1, PURP) # CREATING BUTTONS
    button3 = WORD_FONT.render('[3] CLOTHING',1, PURP)
    win.blit(button1, (30,200))
    win.blit(button2, (30,300)) # PUTTING THE BUTTONS AND INFO ON THE SCREEN
    win.blit(button3, (30,400))
    button1Rect = button1.get_rect()
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    pygame.display.update()
def draw():
    win.fill(WHITE)
    # draw title
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20)) # Notice centering
    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    global score
    global hangman_status
    FPS = 60
    clock = pygame.time.Clock()
    run = True
    INS()
    pygame.time.delay(3000)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
                                score += 1
        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        if won:
            display_message("You WON!")
            SCORE(score)
            break

        if hangman_status == 6:
            display_message("You LOST!")
            SCORE(score)
            break

while True:
    main()
pygame.quit()
