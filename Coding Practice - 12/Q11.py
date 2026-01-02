n = int(input())

for i in range(1,n + 3):
    if i == 1 or i == n + 2:
        row = ("+ ") + ("- ") * n + ("+ ")
        
    else:
        hallow_space = 2 * n 
        
        row = ("| ") + " " * hallow_space + ("| ")
    
    print(row)