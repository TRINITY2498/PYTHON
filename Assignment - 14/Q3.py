n = int(input())

for i in range(1,n + 1):
    cols = i 
    left_space = " " * (n - i)
    print(left_space,end = "")
    
    for j in range(1,cols + 1):
        
        if i == 1 and j == 1:
            print(j,end = " ")
        
        elif j == 1:
            print(j,end = " ")
        
        elif j == cols:
            print(j,end = " ")
        
        else:
            print(" ",end = " ")
            
    print()

for p in range(n - 1,0,-1):
    cols = p 
    left_space = " " * (n - p)
    print(left_space,end = "")
    
    for q in range(1,cols + 1): 
        
        if p == n and q == 1:
            print(q,end = " ")
        
        elif q == 1:
            print(q,end = " ")
        
        elif q == cols:
            print(q,end = " ")
        
        else:
            print(" ",end = " ")
    print()
        
     