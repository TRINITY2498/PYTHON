n = int(input())

for i in range(1,n + 1):
    
    for j in range(1,2 * n):
        
        if j > (n - i) and j <= (n + i - 1):
            
            print("0", end = " ")
        
        else:
            
            print(".",end = " ")
    print()    


for p in range((n - 1), 0, -1):
    
    for q in range(1, (2 * n)):
        
        if q > (n - p) and q <= (n + p - 1):
            
            print("0",end = " ")
        
        else:
            print(".",end = " ")
    
    print()
        
        
        
        
        