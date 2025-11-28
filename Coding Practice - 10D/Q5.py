n = int(input())

for i in range(1,n + 1):
    space = (2 * (n - i))
    stars = i 
    row = (("* ") * stars + "  " * space + "* " * stars)
    print(row)
    
for i in range (1,n):
    space = (2 * i)
    stars = (n - i)
    row = (("* ") * stars + "  " * space + ("* ") * stars)
    print(row)