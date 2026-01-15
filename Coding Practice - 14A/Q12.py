n = int(input())
k = 2

for i in range(1,n + 1):
    left_space = " " * (n - i)
    print(left_space,end = "")
    for j in range(1,i + 1):
        
        if i == 1:
            print(str(j),end = " ")
        
        elif i == n:
            print(str(j),end = " ")
        
        elif j == 1:
            print(str(j),end = " ")
        
        elif i == j:
            print(str(k),end = " ")
            k = k + 1
        
        else:
            print(" ",end = " ")
    print()