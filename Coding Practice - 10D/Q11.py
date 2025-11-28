n = int(input())

for i in range(1,n + 1):
    star = i
    space = n - i 
    row = ((" ") * space + ("* ") * star + (" ") * space)
    print(row)
    
for i in range(1,n):
    space = i 
    star = n - i 
    row = ((" ") * space + ("* ") * star + (" ") * space)
    print(row)