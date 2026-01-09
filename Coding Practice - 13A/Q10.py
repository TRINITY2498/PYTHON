m = int(input())
n = int(input())
d = 0

for i in range(1,m + 1):
    for j in range(0,n):
        d = d + 1
        print(str(d) + " ",end = "")
    print()