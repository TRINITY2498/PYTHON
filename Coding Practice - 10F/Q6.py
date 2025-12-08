n = int(input())

left_space = 0

for i in range(1,n + 1):
    
    if i == 1:
        row = ("* ") * n 
    elif i == n:
        row = (" ") * left_space + ("* ")
    else:
        mid = 2 * (n - i) - 2
        row = (" ") * left_space + ("* ") + (" ") * mid + ("* ")
    
    left_space = left_space + 2 
    print(row)