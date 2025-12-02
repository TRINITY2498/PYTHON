# Hollow Square Pattern

n = int(input())

for i in range(1,n + 1):
    space = (2 * n) - 4
    
    if i == 1 or i == n:
        row = ("* ") * n
    else: 
        row = (("* ") * 1 + (" ") * space + ("* ") * 1)
    print(row)