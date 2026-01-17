n = int(input())
k = 1

for i in range(1,n + 1):
    cols = n - i + 1
    
    for j in range(1,cols + 1):
        
        if i == 1:
            print(j,end = " ")
            k = k + 1
        
        elif i == n and j == 1:
            print(k,end = " ")
            k = k + 1
        
        elif j == 1 or j == (n - i + 1):
            print(k,end = " ")
            k = k + 1
        
        else:
            print(" ",end = " ")
            k = k + 1
    print()