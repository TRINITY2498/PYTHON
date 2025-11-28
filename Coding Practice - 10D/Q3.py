n = int(input())
digit = 1 

for i in range(1,n + 1):
    star = i 
    space = (n - i)
    row1 = ((str(digit) + " ") * star) + (" ") * space 
    digit = digit + 1 
    print(row1)
digit = digit - 1 

for i in range(1,n):
    digit = digit - 1
    star = n - i 
    space = 2 * i 
    row2 = ((str(digit) + " ") * star) + (" ") * space 
    print(row2)