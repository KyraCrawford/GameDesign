#KYRA CRAWFORD

import random
import time

name=input("What is your name? ")
print("Good luck,", name)

gameWords= ['python','java','javaScript','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']

answer = input('Do you want to guess a word? (yes/no) ')

#use choice method of random function to pick a gameWords

while answer == 'yes':
    word = random.choice(gameWords)
    guesses = ''
    turns = 15
    while turns > 0:
        for char in word:
            if char in guesses:
                print(char)
            else:
                print('\b_')
        guess = input('Give me a letter: ')
        guesses += guess
        turns-= 1
        if word in guesses:
            pass
            print('You win!\n\n')
            break
    if turns <= 0:
        print('Sorry, you ran out of guesses. You lose!')
        print('The word was:',word)
    answer = input('Do you want to play again? ')
time.sleep(10)
