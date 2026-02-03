n = int(input())

first_char = 65 
hollow_space_upper = 1 

for i in range(1,n + 1):
    
    left_spaces = " " * (n - i) 
    
    if i == 1:
        print(left_spaces + chr(first_char))
        first_char = first_char + 1 
    
    else:
        
        print(left_spaces + chr(first_char) + " " * hollow_space_upper + chr(first_char))
        hollow_space_upper = hollow_space_upper + 2
        first_char = first_char + 1 
        
first_char = first_char - 1
hollow_space_lower = hollow_space_upper - 4

for j in range(1,n):
    first_char = first_char - 1 
    left_spaces = " " * j
   
    
    if j == n - 1:
        
        print(left_spaces + chr(first_char))
    
    else:
        
        print(left_spaces + chr(first_char) + " " * hollow_space_lower + chr(first_char))
        hollow_space_lower = hollow_space_lower - 2 
        
        