n = int(input())

for i in range(1,n + 1):
    
    for j in range(1,i + 1):
        
        if i == 1:
            
            print("|",end = " ")
        
        elif j == 1:
            
            print("|",end = " ")
        
        elif i == j:
            
            print("\\",end = "")
        
        else:
            
            print(" ",end = "")
        
    print()
    

for p in range(1,n + 1):
    cols = n - p + 1
    
    for q in range(1, cols + 1):
        
        if p == n:
            
            print("|",end = " ")
        
        elif q == 1:
            
            print("|",end = " ")
        
        elif q == cols:
            
            print("/",end = " ")
        
        else:
            
            print(" ",end = "")
    
    print()