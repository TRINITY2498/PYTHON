n = int(input())

for i in range(1,n + 1):
    left_space = (n - i) * 2
    row = (" " * left_space + "* " * i)
    
    print(row)