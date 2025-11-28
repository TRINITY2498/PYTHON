n = int(input())
digit = n 
sec_digit = 1

print(("+ ") * n)

for i in range(1,n):
    space = n - digit
    star = n - sec_digit
    
    row = ((" ") * space + " *" * star + (" ") * space)
    sec_digit = sec_digit + 1 
    digit = digit - 1 
    print(row)