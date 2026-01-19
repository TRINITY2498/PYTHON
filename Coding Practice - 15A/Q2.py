n = int(input())

for i in range(1,n + 1):
    cols = 2 * n
    for j in range(1,cols + 1):
        
        if j <=  i or j > 2 * n - i:
            print("*",end = " ")
        
        else:
            print(" ",end = " ")
    print()

for p in range(n,0,-1):
    cols = 2 * n 
    
    for q in range(1,cols + 1):
        
        if q <= p or q > ((2 * n) - p):
            
            print("*",end = " ")
        
        else:
            print(" ",end = " ")
    print()