m = int(input())
n = int(input())
num = 1

for i in range(1,m + 1):
    for j in range(1,n + 1):
        if i == 1 or i == m:
            print(num,end = " ")
            num = num + 1 
        
        elif j == 1 or j == n:
            print(num,end = " ")
            num = num + 1
        else:
            print(" ",end = " ")
            num = num + 1 
    print()
            