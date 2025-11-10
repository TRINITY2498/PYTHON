n = int(input())
digit = 1
star = 1 

for i in range(1,n + 1):
    space = (n - i) * 2 
    print(" " * space + (str(digit) + " ") * star)
    star = star + 2
    digit = digit + 1 