# pattern: 1 2 3 4 5 6 7 8 9
# 1
#2
#3
#4
#5
#6
#7
#8
#9
# 1
# 2 2
# ...

import sys

numbers = [1,2,3,4,5,6,7,8,9]

for i in numbers:
    print(i,end=" ")
    if i == 9:
        print('\b')

for i in numbers:
    print(i)

def right():
    for i in numbers:
        print((str(i)+' ')* i)
right()

def left():
    for i in numbers:
        print(((str(i) + ' ') * i).rjust(50))

left()

for i in numbers:
    print(((str(i)+' ')* i).rjust(20))
    print(((str(i)+' ')* i).ljust(50))
