n = int(input())

for i in range(1,n + 1):
    left_dots = n - i 
    pyramid = 2 * i - 1
    middle_dots = 2 * (n - i)
    
    for j in range(left_dots):
        
        print(".",end = " ")
    
    for p in range(pyramid):
        
        print("0",end = " ")
        
    for q in range(middle_dots):
        print(".",end = " ")
    
    for k in range(pyramid):
        print("0",end = " ")
    
    for y in range(left_dots):
        
        print(".",end = " ")
   
    print()
        