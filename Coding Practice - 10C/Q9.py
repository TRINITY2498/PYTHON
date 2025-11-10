n = int(input())
digit = n 

for i in range(n):
    space = (i)
    print(" " * space + str(digit) * (n - i))
    digit = digit - 1