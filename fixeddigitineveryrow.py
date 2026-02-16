# Square pattern with provided fixed digit in every row.

n = int(input("Enter no.of rows: "))    # 4
for i in range(n):                      # 0,1,2,3
    print((str(i+1)+' ')*n)