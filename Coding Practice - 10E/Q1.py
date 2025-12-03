n = int(input())


for i in range(1,n + 1):
    if i == 1 or i == n:
        row = ("* ") * n 
    else:
        row = ("* ") + ("0 ") * (n - 2) + ("* ")
    
    print(row)