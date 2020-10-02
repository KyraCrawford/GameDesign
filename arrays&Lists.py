#KYRA CRAWFORD

mylist = [2,4,5,7,8,9]
myfruit=['apple','banana','orange']

newfruit=myfruit.copy()
# myfruit.remove('apple')
print(myfruit)
myfruit.pop(0)
del myfruit[0]
myfruit.append('mango')
myfruit.insert(1,'kiwi')
print(myfruit)
# newfruit.clear() #clears the list but does not completely delete it (things can still be added)
print(newfruit)

#del myfruit will delete the list completely, so you cannot call it anymore
print(mylist[-2])
print(mylist[1:4])

if 4 in mylist:
    print('4 is in MyList')
else:
    print('4 is not in MyList')

# for i in myfruit:
#     mylist.append(i)
# print(mylist) #this way changes to original list, but can be used to join two lists

# myFullList = mylist + myfruit #joining two lists together, creates a new list
# print(myFullList)

mylist.extend(myfruit)
print(mylist) #this way also joins lists, adds to the original list

# tuples
numbers=(1,2,3,4,5)
