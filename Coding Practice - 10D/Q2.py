n = int(input())

for i in range(1,n + 1):
    star = i 
    space = (n - i)
    row_1 = ("* ") * star + (" ") * space
    print(row_1)
    
for i in range(1,n):
    space = 2 * i 
    star = n - (i)
    row_2 = ("* ") * star + (" ") * space
    print(row_2)