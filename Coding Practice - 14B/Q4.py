n = int(input())

k = (n * (n + 1)) // 2

for i in range(1,n + 1):
    cols = n - i + 1 
    
    for j in range(1,cols + 1):
        
        if i == 1:
            print(k,end = " ")
            k = k - 1 
        
        elif j == 1:
            print(k,end = " ")
            k = k - 1
        
        elif j == cols:
            print(k,end = " ")
            k = k - 1 
            
        else:
            print(" ",end = " ")
            k = k - 1 
    print()

