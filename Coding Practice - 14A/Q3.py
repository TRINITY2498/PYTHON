m = int(input())
n = int(input())

for i in range(1,m + 1):
    s = 7
    for j in range(1,n + 1):
        if (i == 1 or i == m or j == 1 or j == n):
            print(str(s), end = " ")
            s += 1 
        else:
            print(" ", end = " ")
            s = s + 1
    print()
        
        