n = int(input())
digit = n

for i in range(n):
    space = i * 2
    token = str(digit) + " "
    print(" " * space + token * (n-i)) 
    digit = digit - 1
    