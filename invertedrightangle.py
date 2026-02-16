# To print Inverted Right Angle Triangle Pattern with * symbols.

n = int(input("Enter no.of rows: "))    # 5
for i in range(n):                      # 0,1,2,3,4
    print('* '*(n-i))