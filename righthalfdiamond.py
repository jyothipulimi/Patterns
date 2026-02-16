# To print Right Half Diamond pattern with '*' Symbols

n = int(input("Enter a number: "))  # 4
for i in range(n):                  # 0,1,2,3
    print('* '*(i+1))
for i in range(n-1):                # 0,1,2
    print('* '*(n-i-1))
