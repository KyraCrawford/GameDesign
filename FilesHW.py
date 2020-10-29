#KYRA CRAWFORD

# HOMEWORK ASSIGNMENT
#ask user for file name, and info to go inside file
#make a menu for creating file(filename), deleting file(filename), adding to file, write in file (give warning about override)
#print what is in file
import os
import time
import sys

name = input('What is your name? ')
welcome = print('\nHello,',name,'\n')
start = input('Would you like to create a file? (y/n) ')

def clear():
    time.sleep(3)
    os.system('cls')

def NEWFILE():
    filename = input('What do you want your file to be named? ')
    FILE = open(filename,'w')
    FILE.write('***THIS IS YOUR FILE***') #default text in your document
    FILE.close()
    print('Your file has been created')
    clear() #clear screen for neatness
    INMENU() #return to menu

def WRITEFILE():
    file = input('What file do you want to write in: ') # user gives file name
    if os.path.exists(file):
        print('\n\n***WARNING*** : If you have already written something in the file, it will be replaced with what you write.') #override warning
        answer = input("\nIf would like to write in the file, reply with 'y', if you wish to simply ADD something to your file, reply with 'n': ") #asking if there are okay with it
        if answer == 'y':
            words = input('What do you want to write in your file: ')
            PEN = open(file,'w')
            PEN.write(words)
            PEN.close()
            print('Your words are in the file,',file,end='.')
            clear()
            INMENU()
        elif answer == 'n':
            ok = input('\n\n*IMPORTANT* When the menu pops up again, select option 3 to add more to your file. (ok)') # proof of life/reading the info
            if ok == 'ok':
                print('Good! You will be returned to the menu shortly.')
                time.sleep(2)
                clear()
                INMENU()
    else:
        print('There is no file called that. You will be returned to the menu shortly.')
        clear()
        INMENU()

def ADDFILE():
    file = input('What file do you want to update: ')
    if os.path.exists(file):
        words = input('What do you want to add to your file: ') #putting the users input into a variable/object
        PENCIL = open(file,'a')
        PENCIL.append(words) #adding users words to file
        PENCIL.close()
        print('"',words,end='" was successfully added to the file,',file) #confirmation for user
        clear()
        INMENU()
    else:
        print('There is no file called that. You will be returned to the menu shortly')
        clear()
        INMENU()

def READFILE():
    file = input('What file do you want me to read/print for you: ')
    if os.path.exists(file):
        EYE = open(file,'r')
        print('This is the contents of the file,',file,end=':\n')
        print(EYE.read())
        answer = input("Let me know when you'er done reading! (ok): ") #allows for time for user to read if they want
        if answer == 'ok':
            print('Great! You will be returned to the menu momentarily.')
            clear()
            INMENU()
    else:
        print('There is no file called that. You will be returned to the menu shortly.')
        clear()
        INMENU()

def DELFILE():
    file = input('What file do you want to delete: ')
    if os.path.exists(file):
        print('Deleting file...') #just aesthetics
        time.sleep(2)
        os.remove(file) #deleting file
        print('File deleted')
        clear()
        INMENU()
    else:
        print('There is no file called that. You will be returned to the menu shortly')
        clear()
        INMENU()

def INMENU():
    print('* * * * * * * * * * * * * * * * *')
    print('*     ~ADDITIONAL OPTIONS~      *')
    print('*   _ _ _ _ _ _ _ _ _ _ _ _ _   *')
    print('*  |                         |  *')
    print('*  |       1. DELETE FILE    |  *')
    print('*  |       2. NEW FILE       |  *')
    print('*  |       3. ADD TO FILE    |  *')
    print('*  |       4. WRITE FILE     |  *')
    print('*  |       5. READ FILE      |  *')
    print('*  |       6. EXIT           |  *')
    print('*  |_ _ _ _ _ _ _ _ _ _ _ _ _|  *')
    print('*                               *')
    print('* * * * * * * * * * * * * * * * *')
    answer = input('What would you like to do? (1/2/3/4/5/6) ')
    if answer== '1':
        clear()
        DELFILE()
    elif answer == '2':
        clear()
        NEWFILE()
    elif answer == '3':
        clear()
        ADDFILE()
    elif answer == '4':
        clear()
        WRITEFILE()
    elif answer == '5':
        clear()
        READFILE()
    elif answer == '6':
        answer = input('Sure you want to exit? (y/n) ')
        if answer == 'y':
            print('Goodbye!')
            time.sleep(4)
            sys.exit()
        elif answer == 'n':
            clear()
            INMENU()

def STARTMENU():
    print('* * * * * * * * * * * * * * * * *')
    print('*        ~FILE CREATION~        *')
    print('*                               *')
    print('*   _ _ _ _  OPTIONS  _ _ _ _   *')
    print('*  |                         |  *')
    print('*  |   1. CREATE/EDIT FILE   |  *')
    print('*  |       2. EXIT           |  *')
    print('*  |_ _ _ _ _ _ _ _ _ _ _ _ _|  *')
    print('*                               *')
    print('* * * * * * * * * * * * * * * * *')

if start == 'y':
    print('')
    STARTMENU()
    answer= input('What would you like to do? (1/2) ')
    if answer == '1':
        clear()
        NEWFILE()
    elif answer == '2':
        clear()
        print('Goodbye!')
        time.sleep(4)
        sys.exit()
else:
    clear()
    print('Goodbye!')
    time.sleep(4)
    sys.exit()
