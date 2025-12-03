m = int(input())
n = int(input())

for i in range(1,m + 1):
    if i == 1 or i == m:
        row = ("* ") * n 
    else:
        row = ("* ") + ("0 ") * (n - 2) + ("* ")
    
    print(row)
        
        