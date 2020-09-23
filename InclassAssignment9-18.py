# KYRA CRAWFORD

# prime number loop
print('The prime numbers between 1 and 72 are:')
for num in range(1,72):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# upside down triangle 5-1 loop
top = 5
for i in range(0, top + 1):
    for x in range(top - i, 0, -1):
        print(x, end=' ')
    print()


# fibonacci loop
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
