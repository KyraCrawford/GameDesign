#KYRA CRAWFORD

import operator

#sort a dictionary descending and ascending by value(1)
dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary:',dict1)
sorted_dict1 = sorted(dict1.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value:',sorted_dict1)
sorted_dict1 = dict( sorted(dict1.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value:',sorted_dict1)

#add a key to an existing dictionary(2)
dict2 = {'Car': 'Honda', 'Name': 'Timothy'}
print(dict2)
dict2.update({'Age': 26})
print(dict2)

#create a new dictionary by concatenating existing dictionaries(3)
NEWDICT = {}
for dict in (dict1, dict2): NEWDICT.update(dict)
print(NEWDICT)

#check if a key is within a dictionary already(4)
dict3 = {'five': 5, 'three': 3, 'four': 4, 'seven': 7}
def key_finder(x):
    if x in dict3:
        print(x,'is already a key in this dictionary.')
    else:
        print(x,'is not a key in this dictionary.')
key_finder('one')
key_finder('seven')

#print dictionary with for loop (5)
for dict_key, dict_value in dict2.items():
    print(dict_key,'is',dict_value)

#print a dicitonary that has a number in x,x*x form (6)
dict4 = {}
n = 4
for x in range (1,n+1):
    dict4[x]=x*x
print(dict4)

#dictionary where the value is the key squared(7)
dict5 = {}
for x in range(1,16):
    dict5[x]=x**2
print(dict5)

#merge dictionaries(8)
mergeDict = dict2.copy()
mergeDict.update(dict3)
print(mergeDict)

#challenge 9 is the same as 5

#find the sum of values in a dictionary
numbers = {'num1':300,'num2':400,'num3':20,'num4':70}
print(sum(numbers.values()))
