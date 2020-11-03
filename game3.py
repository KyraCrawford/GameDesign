# KYRA CRAWFORD
import random, time, os, sys
import datetime

def SCORE(name,score):
    date = datetime.datetime.now()
    with open('SCORE_RECORDS.txt') as s:
        records = open('SCORE_RECORDS.txt','a')
        records.write(str(name))
        records.write(' - ')
        records.write(str(score))
        records.write(' words ')
        records.write(date.strftime('%Y/%m/%d %H:%M'))
        records.write('\n')
        records.close()

def TITLE():
    print('* * * * * * * * * * * * * * * * *')
    print('*       ~GUESS THE WORDS~       *')
    print('*  _ _ _ _ _OBJECTIVE_ _ _ _ _  *')
    print('* |                           | *')
    print('* |    Guess as many words    | *')
    print('* |   correctly as possible!  | *')
    print('* |_ _ _ _ _ _ _ _ _ _ _ _ _ _| *')
    print('*                               *')
    print('*           - RULES -           *')
    print('*    5 lives/turns per word     *')
    print('* ----------------------------- *')
    print('*   Game continues until you    *')
    print('*  fail to guess a word right   *')
    print('* ----------------------------- *')
    print('*  Scores kept in the document  *')
    print("*    called 'SCORE_RECORDS'     *")
    print('*                               *')
    print('* ========= HAVE FUN! ========= *')
    print('*                               *')
    print('* * * * * * * * * * * * * * * * *')
    print('\n')

def clear():
    print('\nLoading next word...')
    time.sleep(2)
    os.system('cls')

name = input("What is your name? ")
start = input('Would you like to play? (y/n) ')

if start == 'y':
    TITLE()
    dict = {}
    with open("WORDBANK.txt") as f:
        for line in f:
            (key, val) = line.split()
            dict[key] = val
    score = 0
    words = list(dict)
    print("Good Luck,", name,end='!\n')

    word = random.choice(words)
    print(word)
    numofwords = (len(dict))
    guesses = ''

    turns = 10
    while turns > 0:
        failedchar = 0
        failedwords = 0
        for char in word:
            if char in guesses:
                print(char,end=' ')
            else:
                print("_",end=' ')
                failedchar += 1
        print('')
        if failedchar == 0:
            # user will win the game if failure is 0
            # and 'You Win' will be given as output
            print("You finished the word!")
            # this print the correct word
            print("The word was: ", word)
            score += 1
            numofwords -= 1
            print('NEXT WORD!')
            clear()
            word = random.choice(words)
            guesses = ''
            failedchar = 0
            if numofwords == 0:
                print('WOW, you guessed all the words correctly!')
                print('Congratulations,',name,end='!\n')
                print('Your score was',score,'out of 10!\n')
                SCORE()
        # if user has input the wrong alphabet then
        # it will ask user to enter another alphabet
        guess = input("\rGuess a letter:")
        # every input character will be stored in guesses
        guesses += guess
        # check input with the character in word
        if guess not in word:
            turns -= 1
            # if the character doesn’t match the word
            # then “Wrong” will be given as output
            print("Wrong")
            # this will print the number of
            # turns left for the user
            print("You have", + turns, 'more guesses')
            if turns == 0:
                print("You ran out of turns!")
                print('The word was: ',word)
                failedwords += 1
                if failedwords == 1:
                    print('GAME OVER!')
                    print('Your score was:',score)
                    print('\n')
                    SCORE()
    start = input('Do you want to play again? (y/n) ')
elif start == 'n':
    print('Had enough fun already?')
    time.sleep(2)
    print('Alright then, bye-bye!')
    print('')
    time.sleep(2)
    sys.exit()
