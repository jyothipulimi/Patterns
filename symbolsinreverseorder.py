# Pyramid pattern with alphabet symbols in reverse of dictionary order in every row.

n = int(input("Enter no.of rows: "))    # 4
for i in range(n):                      # 0,1,2,3
    print(' '*(n-i-1),end=' ')
    for j in range(i+1):                # 1,2,3,4
        print(chr(64+n-j),end=' ')
    print()
