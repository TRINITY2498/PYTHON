# Hollow Pyramid Pattern 

n = int(input())


for i in range(1,n + 1):
    left_space = (n - i)
    mid_space = (2 * i) - 4
    if i == 1: 
        row = ((" ") * (n - 1) + ("* "))
    elif i == n:
        row = ("* ") * n 
    else:
        row = ((" ") * left_space + ("* ") + (" ") * mid_space + ("* "))
    
    print(row)