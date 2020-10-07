#KYRA CRAWFORD
#skip number 16
#NUMBERS 17-24

#unzip list of tuples into own lists (17)
listofTups = [(1,20), (34,7), (19,62)]
print(list(zip(*listofTups)))

#reverse a tuple (18)
tupley = (3,6,1,8,5,10,39)
print(tupley)
print(tupley[::-1])

#convert a list of tuples into dictionary (19)
print(dict(listofTups))

#print a tuple with string formatting (20)
print('This is a tuple:',tupley)

#replace last of duples in a list (21)
listofTups2 = [(16, 24, 990), (90, 32, 'HELLO'), (7, 'ok', 'free')]
print(listofTups2)
listofTups2new = [(16, 24, 25), (90, 32, 25), (7, 'ok', 25)]

listofTups2.clear()
listofTups2 = listofTups2new
print(listofTups2)

#remove empty tuple from list of tuples (22)
listofTups3 = [(), ('1', 'b'), ('a', '2', '7'), ('9')]
listofTups3.pop(0)
print(listofTups3)

#sort tuple with by its float(23)
#???? idk what to do here

#count items in list until the next item is a tuple
LIST = ['no', 'ok', 'cool', 'quick', (0,3), 'dog', 'house']
count = LIST.count(str)
print(count)
if str == tuple:
    print('This is a tuple')
#this is not working, idk why it is giving me an error
