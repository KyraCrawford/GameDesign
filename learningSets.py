#KYRA CRAWFORD

thisset = {'banana','orange','apple','blueberry'}
for x in thisset:
    print(x)

#.add() allows for one element at a time
thisset.update('mango','kiwi', 'melon') #update() allows you to add multiple elements at once

for x in thisset:
    print(x)

print(len(thisset))

otherset = {'watermelon','grapes','kiwi'}
anotherset = {'papaya','green apple','apple'}

print(thisset.union(otherset)) #combine the sets
print(thisset.intersection(anotherset)) # find what is in common with these two sets
