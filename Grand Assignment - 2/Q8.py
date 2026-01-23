n = int(input())

for i in range(n,0,-1):
    
    left_space = " " * (n - i)
    
    print(left_space + "* " * i)

for j in range(1,n):
    left_space = " " * (n - j - 1)
    
    print(left_space + "* " * (j + 1))