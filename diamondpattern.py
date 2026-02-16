# To Print Diamond Pattern

n = int(input("Enter n value: "))   # 4
for i in range(n):                  # 0,1,2,3
    print(' '*(n-i-1)+'* '*(i+1))
for i in range(n-1):                  # 0,1,2
    print(' '*(i+1)+'* '*(n-i-1))
