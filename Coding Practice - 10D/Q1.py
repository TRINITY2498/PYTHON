n = int(input())

for i in range(1,n + 1):
    stars = i 
    space = (n - i) * 4 
    row = ("* ") * stars + (" ") * space + ("* ") * stars
    print(row)