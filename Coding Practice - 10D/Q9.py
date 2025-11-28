n = int(input())
digit = n 
digit_two = 0
for i in range(1,n + 1):
    space = n - digit
    star = n - digit_two
    row = ((" ") * space + ("* ") * star + (" ") * space)
    print(row)
    digit = digit - 1 
    digit_two = digit_two + 1