n = int(input())

for i in range(1,n + 1):
    stars = ("* ") * (2 * (n - i) + 1)
    left_spaces = ("  ") * ((i - 1) * 2)
    
    print(left_spaces + stars)