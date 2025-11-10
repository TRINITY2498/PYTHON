n = int(input())
star = 1 

for i in range(1,n + 1):
    space = (n - i) * 2 
    print((" " * space) + ( star * "* "))
    star = star + 2