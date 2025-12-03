n = int(input())


for i in range(1,n + 1):
    mid_space = (2 * i) - 4 
    right_space = (n - i) * 2
    
    if i == 1:
        row = ("* ")
    elif i == n:
        row = ("* ") * n 
    else: 
        row = ("* ") + (" ") * mid_space + ("* ") + (" ") * right_space
    
    print(row)