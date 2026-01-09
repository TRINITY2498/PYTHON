n = int(input())

for i in range(0,n):
    d = 0
    for j in range(n,i,-1):
        d = d + 1 
        row = ((str(d) + " "))
        print(row, end = "")
    print()