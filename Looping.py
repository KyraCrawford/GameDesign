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

print('The prime numbers between 1 and 72 are:')
for num in range(1,72):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
top = 5
for i in range(0, top + 1):
    for x in range(top - i, 0, -1):
        print(x, end=' ')
    print()
numterms = 9
a = 0
b = 1
sum = 0
count = 0
print("Fibonacci Series: ", end = "\n")
while(count <= numterms):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b
