n = int(input())

digit = 0
count = 0
space = 0 
for i in range(1,n + 1):
    star = n - digit 
    row = ((" ") * space + ("* ") * star)
    print(row)
    space = space + 2
    digit = digit + 1 