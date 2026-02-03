n = int(input())

for i in range(1,n + 1):
    
    spaces = " " * (n - i) 
    
    if i == 1:
        
        row = spaces + (chr(i + 64) + " ")
    
    else:
        
        hollow_space = "  " * (i - 2)
        
        row = spaces + (chr(i + 64) + " ") + hollow_space + (chr(i + 64) + " ")
    
    middle_space = " " * (n - i)
    
    print(row + middle_space + row)
        