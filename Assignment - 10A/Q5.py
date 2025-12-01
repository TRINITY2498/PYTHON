n = int(input())

digit = 0

for i in range(1,n + 1):
    digit = digit + 1
    space = n - i 
    row = ((" ") * space + ((str(digit) + " ") * i) + (" ") * space)
    print(row)
     

for i in range(1,n):
    digit = digit - 1 
    space = i
    row = ((" ") * space + ((str(digit) + " ") * (n - i)) + (" ") * space)
    print(row)
    