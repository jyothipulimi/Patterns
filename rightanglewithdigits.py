# Inverted Right Angle Triangle pattern with digits in ascending order in every row.

n = int(input("Enter no.of rows: "))    # 4
for i in range(n):                      # 0,1,2,3
    for j in range(n-i):                # 4,3,2,1
        print(j+1,end=" ")
    print()