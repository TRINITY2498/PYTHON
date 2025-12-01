n = int(input())

space = 0

print(("* ") * ((2 * n) - 1))

for i in range(1,n):
    star = (n - i)
    
    side_space = i
    row = ((" ") * side_space + ("* ") * star + (" ") * space + ("* ") * star + (" ") * side_space)
    
    space = space + 2
    print(row)