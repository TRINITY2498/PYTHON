s = int(input())
n = int(input())

for i in range(1,n + 1):
    cols = n - i + 1 
    left_space = " " * (i - 1)
    print(left_space,end = "")
    
    for j in range(1,cols + 1):
        
        if i == 1:
            print(s,end = " ")
            s = s + 1 
        
        elif j == 1 or j == cols:
            print(s,end = " ")
            s = s + 1
        
        elif i == n and j == 1:
            print(s,end = " ")
            s = s + 1 
        
        else:
            print(" ",end = " ")
            s = s + 1
            
    print()