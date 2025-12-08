n = int(input())

for i in range(1,n + 1):
    left_space = n - i
    mid = (2 * i) - 4
    if i == 1:
       row = ((" ") * left_space + ("* "))
    elif i == n:
        row = ("* ") * n
    else: 
         row = ((" ") * left_space + ("* ") + (" ") * mid + ("* "))
    
    print(row)