s = int(input())
n = int(input())
k = (n * (n + 1)) // 2 
x = k + s - 1 

for i in range(0,n):
    for j in range(n,i,-1):
        print(str(x) + " ",end = "")
        x = x - 1
    print()