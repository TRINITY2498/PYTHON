m = int(input())
n = int(input())

k = m * n 

for i in range(1,m + 1):
    
    for j in range(1,n + 1):
        
        if i == 1 or i == m:
            print(k,end = " ")
            k = k - 1 
        
        elif j == 1 or j == n:
            print(k,end = " ")
            k = k - 1 
        
        else:
            print(" ",end = " ")
            k = k - 1
    print()
        