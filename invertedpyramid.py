# To print Inverted Pyramid pattern with alphabet symbols in dictionary order in every row.

n = int(input("Enter no.of rows: "))    # 4
for i in range(n):                      # 0,1,2,3
    print(' '* i, end=' ')
    for j in range(n-i):
        print(chr(65+j), end=' ')
    print()
