# Right angle triangle pattern with fixed alphabet symbol in every.

n = int(input("Enter no.of rows: "))    # 4
for i in range(n):                      # 0,1,2,3
    print((chr(65+i)+' ')*(i+1))