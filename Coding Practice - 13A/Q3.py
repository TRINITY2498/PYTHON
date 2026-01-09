m = int(input())
n = int(input())

d = 6

for i in range(1,m + 1):
    for j in range(1,n + 1):
        print(str(d + j) + " ",end = "")
    print()