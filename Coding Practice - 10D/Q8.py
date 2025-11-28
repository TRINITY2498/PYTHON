n = int(input())
digit = n 

for i in range(1,n + 1):
    space = n - i 
    star = n - digit 
    row = ((" ") * space + ("* ") * star + (" ") * space)
    print(row)
    digit = digit - 1
    