#KYRA CRAWFORD

import random
import time

name=input("What is your name? ")

gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']

answer = input('Do you want to guess a word? (yes/no) ')

#use choice method of random function to pick a gameWords

while answer == 'yes':

    print("Good luck,", name)
    word = random.choice(gameWords)
    guesses = ''
    turns = 10
    while turns > 0:
        for char in word:
            if char in guesses:
                print(char,end=' ')
            else:
                print('_',end=' ')
        guess = input('\nGive me a letter: ')
        guesses += guess

        if guess not in word:
            turns -= 1
            print('Wrong!')
            print('You have',turns,'guesses left.')
        if turns == 0:
            print('You lose! Better luck next time.')
            print('The word was:',word)
    answer = input('Do you want to play again? ')
time.sleep(10)
 #i can't fiugre out the game mechanics
