s = int(input())
n = int(input())
d = s 

for i in range(1,n + 1):
    for j in range(0,2 * i):
        print(str(d) + " ",end = "")
        d = d + 1
    print()