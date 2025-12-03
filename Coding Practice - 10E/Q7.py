n = int(input())

for i in range(1,n + 2):
    space = (n + 1) - i
    if i == 1:
        row = ("_") * (n + 1) 
    else: 
        row = ("|") + (" ") * space + ("/") 
    
    print(row)