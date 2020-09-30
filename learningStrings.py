#KYRA CRAWFORD

strVar = 'My name is K'

print(strVar)
print(len(strVar))
print(strVar[len(strVar)-1])

indexNum = strVar.find('name')
print(indexNum)
print(strVar[indexNum: indexNum + 4])
print(strVar[indexNum: ])
print(strVar[ :indexNum +1])
print(strVar.replace('name', 'initial'))
strVar= strVar.replace('name','initial')
print(strVar)

print(strVar.upper())
print(strVar.lower())

back = list(strVar)
print(back)
