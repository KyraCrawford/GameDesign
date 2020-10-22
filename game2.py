# KYRA CRAWFORD

# translating game (chinese to english)
import time

name=input("What is your name? ")

adj = {'tall':'gāo', 'small':'xiǎo', 'big':'dà', 'good':'hǎo', 'fast':'kuài', 'old':'lǎo', 'long':'chǎng', 'fat':'pàng', 'slow':'màn', 'short':'duǎn'}
verb = {'throw':'diū', 'stand up':'qǐ lái', 'sit down':'zuò', 'run':'pǎo bù', 'walk':'bù xíng', 'sleep':'shuì jiào', 'eat':'chī', 'write':'xiě', 'drink':'hē', 'go to':'qù'}
hobby = {'swimming':'yóuyǒng','play basketball':'dǎ lán qiú','play soccer':'tī zú qiú','play video games':'wán diàn wán','watch TV':'kàn diàn shì','play outside':'chū qù wán','drawing':'huà huà','go online':'shàng wǎng','play ping pong':'dǎ pīng pāng qiú','watch a movie(@ theater)':'kàn diàn yǐng'}

def GAME():
    score = 0
    rounds = 10
    print('')
    print('GOOD LUCK,',name,end='!')
    def word_bank():
        print('\nWORD BANK:')
        for key,value in set.items():
            print('|',key,end=' ')
        print('')
    for key, value in set.items():
        word = value
        correct = key
        word_bank()
        print('What do you think the Mandarin word,',word,end=', is in English?')
        answer=input('\nAnswer: ')
        if answer == correct:
            print('Correct!\n')
            score += 1
            rounds -= 1
        else:
            print('Incorrect!\n')
            rounds -= 1
        if rounds == 0:
            print('Your score was',score,'out of 10!')
            if score >= 5:
                print('Congratualations',name,end='!')
                print(' YOU WON!!\n')
            else:
                print("Unfortunately, you didn't guess enough words correctly to win. Good game, though!\n")
    time.sleep(5)
    start=input('Do you want to play again? (yes/no) ')

def MENU():
    print("* * * * * * * * * * * * * * *")
    print('*    Guess word meanings    *')
    print('*   ~~ Chinese Edition ~~   *')
    print('*                           *')
    print("*   _ Select a word set _   *")
    print('*  |                     |  *')
    print('*  |    1. ADJECTIVES    |  *')
    print('*  |    2. VERBS         |  *')
    print('*  |    3. HOBBIES       |  *')
    print('*  | _ _ _ _ _ _ _ _ _ _ |  *')
    print('*                           *')
    print('*        How to win:        *')
    print('*      Guess 5 or more      *')
    print('*  word meanings correctly  *')
    print('* * * * * * * * * * * * * * *')

start=input('Would you like to play? (yes/no) ')

if start == 'yes':
    score = 0
    print('')
    MENU()
    set = input('Which word set do you want to play with? (1/2/3) ')
    if set == '1':
        set = adj
        print('You chose the ADJECTIVES word set.')
        GAME()
    elif set == '2':
        set = verb
        print('You chose the VERBS word set.')
        GAME()
    elif set == '3':
        set = hobby
        print('You chose the HOBBIES/ACTIVITIES word set.')
        GAME()
