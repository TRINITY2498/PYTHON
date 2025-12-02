# Hollow Right Angle Triangle 

n = int(input())


for i in range(1,n + 1):
    
    if i == 1:
        row = ((" ") * ((2 * n ) - 2)) + ("* ") 
    elif i == n:
        row = ("* ") * n 
    else:
        left_space = ((2 * n) - (2 * i))
        mid_space = ((2 * i) - 4)
        
        row = ((" ") * left_space + ("* ") + (" ") * mid_space + ("* "))
        
    print(row)