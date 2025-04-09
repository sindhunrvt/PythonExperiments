
rows = int(input("Enter the number of rows: "))
#cols = int(input("Enter the number of columns: "))
for n in range(1,rows+1):
    for c in range(1,n+1):
        print(c, end=' ')
    print(' ')

rows = int(input("Enter the number of rows: "))
#cols = int(input("Enter the number of columns: "))
for n in range(1,rows+1):
    for c in range(1,n+1):
        print(n*c, end=' ')
    print(' ')

rows = int(input("Enter the number of rows: "))
#cols = int(input("Enter the number of columns: "))
for n in range(1,rows+1):
    for c in range(1,n+1):
        print('*', end=' ')
    print(' ')
