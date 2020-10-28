# KYRA CRAWFORD 10/28/2020
#learn about files: how to write('w'), read('r'), close, and append ('a') files

import os
import time

#creata a fileVariablName = open('filename.txt', function)
#write function is w
myFile = open('newFile.txt', 'w') #open file if it exists, if not it will create a new file
myFile.write('Hello there.') #putting 'Hello there.' in the file
myFile.close() #every time you open a file you should close it
myFile = open('newFile.txt', 'r') #open file again to read it
print(myFile.read())
myFile.close()
myFile = open('newFile.txt', 'w') #open file if it exists, if not it will create a new file
myFile.write('How has your day been?\n') #this line will replace the previous one
myFile.close() #every time you open a file you should close it
myFile = open('newFile.txt', 'r') #open file again to read it
print(myFile.read())
myFile.close()
myFile = open('newFile.txt', 'a') #the a stands for append, append adds more lines (not deleting the previous lines)
myFile.write('I like chicken.\n')
myFile.close() #every time you open a file you should close it
myFile = open('newFile.txt', 'r') #open file again to read it
print(myFile.read())
myFile.close()

#to delete a file use the os library
time.sleep(2) #wait 2 seconds
os.remove('newFile.txt')

#checking if a folder/file/file path exists
# ***doulbe back slash is needed for full paths*** (instead of C:\Users\... it is C:\\Users\\...)
if os.path.exists('stringsFun.py'):
    print('yes')
else:
    print('no')

myFile = open('lineFile.txt', 'w')
for i in range(10):
    word = 'This is line number: ' + str(i+1) + '\r\n'
    myFile.write(word)
myFile.close()
myFile = open('lineFile.txt', 'r')
print(myFile.read())
myFile.close()

# HOMEWORK ASSIGNMENT
#ask user for file name, and info to go inside file
#make a menu for creating file(filename), deleting file(filename), adding to file, write in file (give warning about override)
#print what is in file
