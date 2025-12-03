m = int(input())
n = int(input())

for i in range(1,m + 1):
    space = (2 * n) - 4
    if i == 1 or i == m: 
        row = ("* ") * n 
    else:
        row = ("* ") + (" ") * (space) + ("* ")
    
    print(row)