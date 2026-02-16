# Right Half Diamond pattern with alphabet symbols in dictionary order in every row.

n = int(input("Enter n value: "))       # 4
for i in range(n):                      # 0,1,2,3
    for j in range(i+1):
        print(chr(65+j), end=' ')
    print()
for i in range(n-1):                    # 0,1,2
    for j in range(n-i-1):
        print(chr(65+j), end=' ')
    print()