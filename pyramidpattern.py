# To print pyramid pattern with fixed digit in every row.

n = int(input("Enter no.of rows: "))            # 4
for i in range(n):                              # 0,1,2,3
    print(' '*(n-i-1) + (str(i+1)+' ')*(i+1))