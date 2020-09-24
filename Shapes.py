#KYRA CRAWFORD

rows = int(input('Please type a number: \n'))


for line in range (rows):
    print()

    for number in range (line+1):
        print('*', end = '')

    for space in range (rows-line-1):
        print(' ', end = '')

    for number in range (rows-line):
        print('*', end ='')

    for space in range (line):
        print(' ', end = ' ')

    for number in range (rows-line):
        print('*', end ='')

    for space in range (rows-line-1):
        print (' ',end = '')

    for number in range (line+1):
        print('*', end = '')
