n = int(input())

for i in range(1,n + 1):
    left = (i - 1)
    right = (i - 1)
    if i == 1:
        row = ("* ") * n 
    elif i == n:
        row = (" ") * left + ("*") + (" ") * right
    else: 
        mid = 2 * (n - i) - 2
        row = (" ") * left + ("* ") + (" ") * mid + ("* ") + (" ") * right
    
    print(row)
    