# Kyra Crawford

numbers = [1,2,3,4,5,6,7,8,9]

for i in numbers:
    print(i,end=" ")
    if i == 9:
        print('\b')

for i in numbers:
    print(i)

for i in numbers:
        print((str(i)+' ')* i) #right side

for i in numbers:
        print(((str(i) + ' ') * i).rjust(50)) #left side

for i in numbers:
    print((((((str(i)+' ')* i).rjust(25)+ (' ') + (str(i)+' ')* i)))) #full pyramid with middle space
