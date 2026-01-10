s = int(input())
n = int(input())

k = n * (n + 1) // 2

x = k + s - 1 

for i in range(1,n + 1):
    for j in range(1,i + 1):
        print(str(x) + " ",end = "")
        x = x - 1
    print()