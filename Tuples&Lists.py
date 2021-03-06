#KYRA CRAWFORD

from copy import deepcopy

#tuple (1)
numbers = (1, 2, 3)
print(numbers)

#tuple with mixed data types (2)
mixed_tuple = (9, "Hello", 36.8)
print(mixed_tuple)

#print on number in tuple (3)
print(numbers[2])

# unpacking tuple into variables (4)
x,y,z = mixed_tuple
print(x)
print(y)
print(z)

# add an item to a tuple (5)
mixed_tuple = mixed_tuple + (29,)
print(mixed_tuple)

#cahnge tuple to string (6)
morenumbers = (2,4,5,8,1,0,8,5,4,5,3,10,13)
str = str(morenumbers)
print(str)

# find 4th and 4th to last item in tuple (7)
random_tuple = ('y',6,89,11,5,'a','l',2,'b',34)
item1 = random_tuple[3]
item2 = random_tuple[-4]
print(item1)
print(item2)

#clone a tuple (8)
rantuple_clone = deepcopy(random_tuple)
print(rantuple_clone)

#find repeated numbers (9)
for x in morenumbers:
    count = morenumbers.count(x)
    if count > 1:
        print(x, 'is repeated')

#check if element is in a tuple (10)
print(3 in mixed_tuple)

#convert list to tuple (11)
List = ['red','green','blue','orange']
print(List)
List = tuple(List)
print(List)

#remove item from tuple (convert to list, remove,convert back)(12)
random_tuple = list(random_tuple)
random_tuple.remove('b')
random_tuple = tuple(random_tuple)
print(random_tuple)

#slice a tuple (13)
slice = morenumbers[6:] #from 6 index to end of tuple
print(slice)

#find index of an item in tuple (14)
index = List.index('red')
print('The word "red" is located at:',index)

#find size or length of a tuple (15)
print(len(mixed_tuple))
