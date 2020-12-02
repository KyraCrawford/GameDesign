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
# words = levelpick
words = CLOTHING
word = random.choice(words)
guessed = []

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
PURP = (114, 40, 189)

def SCORE(score):
    date = datetime.datetime.now()
    with open('SCORE_RECORDS_HM.txt') as s:
        records = open('SCORE_RECORDS_HM.txt','a')
        records.write(str(score))
        records.write(' wrong letters ')
        records.write(date.strftime('%Y/%m/%d %H:%M'))
        records.write('\n')
        records.close()
def MENU():
    global words
    global FRUITS, GADGETS, CLOTHING
    win.fill(WHITE)
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    instruction = TITLE_FONT.render('HOW TO PLAY\nSELECT A WORD LIST FROM BELOW\nTRY TO GUESS THE LETTERS IN EACH WORD\nSCORES ARE RECORDED IN SCORE_RECORDS_HM.txt\n**THE LOWER THE SCORE THE BETTER**',1, BLACK)
    button1 = WORD_FONT.render("FRUITS",1, PURP)
    button2 = WORD_FONT.render('GADGETS',1, PURP)
    button3 = WORD_FONT.render('CLOTHING',1, PURP)
    win.blit(instruction,(40,50))
    win.blit(button1, (30,200))
    win.blit(button2, (30,300))
    win.blit(button3, (30,400))
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
            if dis < RADIUS:
                words = FRUITS
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
    MENU()
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
