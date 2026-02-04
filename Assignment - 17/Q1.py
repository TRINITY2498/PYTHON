n = int(input())
star = 65

for i in range(1,n + 1):
    left_space = " " * (n - i) 
    hollow_space = " " * (2 * (i - 1) - 1)
    
    if i == 1:
        
        print(left_space + (chr(star) + " "))
        star = star + 1 
    
    else:
        
        print(left_space + chr(star) + hollow_space + chr(star + 1))
        star = star + 2 
        
star = star - 4 

for j in range(1,n):
    left_space = " " * (j) 
    hollow_space = " " * (2 * (n - j) - 3)
    
    if j == (n - 1):
        
        star = star + 1
        print(left_space + chr(star))
    
    else:
        
        print(left_space + chr(star) + hollow_space + chr(star + 1))
        star = star - 2
        
    
        
        
    
    