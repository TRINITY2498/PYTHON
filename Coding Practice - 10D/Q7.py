n = int(input())

digit = 1 

for i in range(1,n + 1):
    space = n - i 
    star = i 
    row = ((" ") * space + (str(digit) + " ") * star + (" ") * space)
    digit = digit + 1 
    print(row)