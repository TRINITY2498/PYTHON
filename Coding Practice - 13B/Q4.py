m = int(input())
n = int(input())
d = m * n 

for i in range(1,m + 1):
    for j in range(1,n + 1):
        print(str(d) + " ",end = "")
        d = d - 1 
    print()
    