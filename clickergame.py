import pygame
import sys
import time
import random
import math
import random
import os
import datetime
level = ''
run = False
menu = True
black = (0,0,0)
white = (255,255,255)
purp = (114, 40, 189)
result = 0
timeleft = 0
leveltime = 0
pygame.init()
width = 1000
height = 800 # setting screen parameters
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('CLICKITY CLICK CLICK')
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60) #setting fonts
TITLE_FONT = pygame.font.SysFont('comicsans', 70)
INS_FONT = pygame.font.SysFont('comicsans', 25)
# function for score keeping and leaderboard
def SCORE(result):
    global level
    date = datetime.datetime.now()
    with open('SCORE_RECORDS_CLICK.txt') as s:
        records = open('SCORE_RECORDS_CLICK.txt','a')
        records.write(str(result))
        records.write(' clicks on ')
        records.write(str(level))
        records.write(' difficulty ')
        records.write(date.strftime('%Y/%m/%d %H:%M'))
        records.write('\n')
        records.close()
def show_result(text):
    global background
    background = (random.randint(50,255), random.randint(50,255), random.randint(50,255))
    set_background(background)
    font = pygame.font.Font(None, 50)
    text = font.render(' '*100+str(text)+' '*100, True, (0, 0, 0), background)
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx #centering
    textRect.centery = screen.get_rect().centery #centering
    screen.blit(text, textRect)
    pygame.display.update()
def show_time(time):
    font = pygame.font.Font(None, 25)
    text = font.render('Time left(seconds): '+str(time)+' '*100, True, black, background)
    textRect = text.get_rect()
    textRect.x = screen.get_rect().x+5
    textRect.y = screen.get_rect().y+5
    screen.blit(text, textRect)
    pygame.display.update()
#background changing function
def set_background(bg):
    screen.fill(bg)
    pygame.display.flip()
# creating the easy gamemode
def mainEasy():
    global timeleft
    global run
    global level
    global leveltime
    timeleft = 60
    leveltime = 60
    level = 'EASY'
    run = True
# creating the medium gamemode
def mainMedium():
    global timeleft
    global run
    global level
    global leveltime
    timeleft = 45
    leveltime = 45
    level = 'MEDIUM'
    run = True
# creating the hard gamemode
def mainHard():
    global timeleft
    global run
    global level
    global leveltime
    timeleft = 30
    leveltime = 30
    level = 'HARD'
    run = True
# open the leaderboard for the LEADERBOARD button
def leaderboard():
    os.system('SCORE_RECORDS_CLICK.txt')

def MENU(menu):
    while menu:
        #creating the buttons
        button_1 = pygame.Rect(100,600,200,50)
        button_2 = pygame.Rect(400,600,200,50)
        button_3 = pygame.Rect(700,600,200,50)
        button_4 = pygame.Rect(150,695,365,50)
        button_5 = pygame.Rect(540,695,250,50)
        mx, my = pygame.mouse.get_pos()
        screen.fill(white)
        # rectangles for buttons
        pygame.draw.rect(screen, (purp), button_1)
        pygame.draw.rect(screen, (purp), button_2)
        pygame.draw.rect(screen, (purp), button_3)
        pygame.draw.rect(screen, (purp), button_4)
        pygame.draw.rect(screen, (purp), button_5)
        text1 = TITLE_FONT.render("CLICKITY CLICK CLICK", 1, black)
        screen.blit(text1, (int(width/2 - (text1.get_width()/2)), 100))
        text2 = INS_FONT.render("HOW TO PLAY:", 1, black)
        screen.blit(text2, (int(width/2 - text2.get_width()/2), 190))
        text2_0 = INS_FONT.render("Click the screen as many times as possible!", 1, black)
        screen.blit(text2_0, (int(width/2 - text2_0.get_width()/2), 240))
        text2_1 = INS_FONT.render("The amount of time you have to click", 1, black)
        screen.blit(text2_1, (int(width/2 - text2_1.get_width()/2), 290))
        text2_2 = INS_FONT.render("is determined by the level you pick.", 1, black)
        screen.blit(text2_2, (int(width/2 - text2_2.get_width()/2), 340))
        text2_3 = INS_FONT.render("The higher the difficulty, the less time you have.", 1, black)
        screen.blit(text2_3, (int(width/2 - text2_3.get_width()/2), 390))
        text2_4 = INS_FONT.render('The score records are kept on the file, "SCORE_RECORDS_CLICK".',1,black)
        screen.blit(text2_4, (int(width/2 - text2_4.get_width()/2),440))
        text2_5 = INS_FONT.render('[Auto-Clickers are NOT permitted]',1,black)
        screen.blit(text2_5,(int(width/2 - text2_5.get_width()/2),490))
        textWarn = LETTER_FONT.render('**SEIZURE WARNING - FLASHING COLORS**',1,(255,0,0))
        screen.blit(textWarn,(int(width/2 - textWarn.get_width()/2),550))
        text3 = WORD_FONT.render("EASY", 1, black)
        screen.blit (text3, (int(width/5 - text3.get_width()/2), 605))
        text4 = WORD_FONT.render("MEDIUM", 1, black)
        screen.blit(text4, (int(width/2 - text4.get_width()/2), 605))
        text5 = WORD_FONT.render("HARD", 1, black)
        screen.blit(text5, (int(width/1.25 - text5.get_width()/2), 605))
        text6 = WORD_FONT.render("LEADERBOARD", 1, black)
        screen.blit(text6, (int(width/3 - text6.get_width()/2), 700))
        text7 = WORD_FONT.render("[ESC] EXIT", 1, black)
        screen.blit(text7, (int(width/1.5 - text7.get_width()/2), 700))
        cursorpic = pygame.image.load('clicker\cursor.png')
        screen.blit(cursorpic,(725,120))
        leftlook = pygame.image.load('clicker\ok.png')
        screen.blit(leftlook,(100,280))
        rightlook = pygame.image.load('clicker\chad.png')
        screen.blit(rightlook,(730,280))
        top = pygame.image.load('clicker\shrek.png')
        screen.blit(top,(int(width/2 - top.get_width()/2),25))
        by = INS_FONT.render('A GAME BY KYRA CRAWFORD',1,black)
        screen.blit(by,(65,780))
        bottom = pygame.image.load('clicker\dog2.png')
        screen.blit(bottom,(0,750))
        pygame.display.update()
        event = pygame.event.poll()
            # code behind clicking the buttons
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
        if button_1.collidepoint((mx,my)):
            if click:
                screen.fill(black)
                pygame.display.update()
                menu= False
                mainEasy()
                pass
        if button_2.collidepoint((mx,my)):
            if click:
                screen.fill(black)
                pygame.display.update()
                menu =False
                mainMedium()
                pass
        if button_3.collidepoint((mx,my)):
            if click:
                screen.fill(black)
                pygame.display.update()
                menu =False
                mainHard()
                pass
        if button_4.collidepoint((mx,my)):
            if click:
                pygame.quit()
                leaderboard()
                pass
        if button_5.collidepoint((mx,my)):
            if click:
                pygame.quit()
        keyBoardKey = pygame.key.get_pressed()
        if keyBoardKey[pygame.K_ESCAPE]:
            pygame.quit()
        if event.type == pygame.QUIT:
            run=False
            sys.exit()
        click = False
MENU(True)
while run:
    MENU(False)
    background = (255,255,255)
    set_background(background)
    screen.fill(background)
    pygame.display.flip()
    level = level
    leveltime = leveltime
    timeleft = timeleft
    result = 0
    while True:
        if result == 0:
            timestart = int(time.time())
        show_time(timeleft)
        if result>=0 and timeleft>0:
            timeleft = (int(leveltime))-(int(time.time())-timestart)
            show_time(timeleft)
        elif result>=0 and timeleft<=0:
            show_result('You got this many clicks: '+str(result)+'. GOOD JOB!')
            nice = pygame.image.load('clicker/nicework.png')
            screen.blit(nice,(int(width/2 - nice.get_width()/2),270))
            pygame.display.update()
            time.sleep(3)
            SCORE(result)
            run = False
            MENU(True)
            break
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            run=False
            sys.exit()
        elif pygame.mouse.get_pressed()[0] and event.type == pygame.MOUSEBUTTONDOWN:
                result += 1
                show_result(result)
        run = False
