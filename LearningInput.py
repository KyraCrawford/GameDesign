# KYRA CRAWFORD

#asking the user for a value
#the default for user input is a string
#we can use type casting to turn it into an integer

begin = 5

lines = begin

for line in range (lines):
    for number in range(begin-line,0,-1):
        print(number, end=' ')
    print()
