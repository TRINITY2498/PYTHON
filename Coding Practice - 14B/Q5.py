s = int(input())
n = int(input())

for i in range(1,n + 1):
    cols = i 
    
    for j in range(1,cols + 1):
        
        if i == 1:
            print(s,end = " ")
            s = s + 1
        
        elif j == 1:
            print(s,end = " ")
            s = s + 1 
        
        elif j == cols:
            print(s,end = " ")
            s = s + 1 
        
        elif i == n:
            print(s,end = " ")
            s = s + 1 
            
        else:
            print(" ",end = " ")
        
    print()