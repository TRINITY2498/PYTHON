n = int(input())

for i in range(1,n + 1):
    left_space = n - i 
    row = (" " * left_space + "* " * i)
    print(row)
    
for i in range(1,n):
    mid = 2 * (n - i) - 4 
    left_space = i
    if i == (n - 1):
        row = (" " * i + "* ")
    else:
        row = (" " * left_space + "* " + " " * mid + "* ")
    
    print(row)