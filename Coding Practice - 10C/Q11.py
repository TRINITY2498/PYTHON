n = int(input())
star = (2 * n) - 1 

for i in range(n):
    space =  i
    print(" " * space + "*" * (star))
    star = star - 2
    