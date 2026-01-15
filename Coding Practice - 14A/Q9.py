n = int(input())
k = n - 1 

for i in range(1,n + 1):
    cols = n - i + 1 
    left_space = " " * (i - 1)
    print(left_space,end = "")
    
    for j in range(1,cols + 1):
        
        if i == 1:
            print(j,end = " ")
            
        elif j == 1:
            print(j,end =" ")
        
        elif j == cols:
            print(k,end = " ")
            k = k - 1 
        else:
            print(" ",end = " ")
    print()