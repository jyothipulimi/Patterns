# To print Right Half Diamond pattern with '*' Symbols

n = int(input("Enter a number: "))
for i in range(n):
    print('* '*(i+1))
for i in range(n-1):
    print('* '*(n-i-1))
