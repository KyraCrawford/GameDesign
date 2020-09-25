#KYRA CRAWFORD
#learning about functions

def test_function():
    print('1 2 3 4 5 6 7 8 9')

def name(lines):
    line=int(lines)
    for i in range(lines):
        print('Hi, my name is Kyra')

def loops_rows_col(row,col):
    for rows in range(row):
        for cols in range(col):
            print('*', end='')
        print()

x = 4
print(x)

loops_rows_col(5,10)
name(2)
for y in range(3):
    test_function()
