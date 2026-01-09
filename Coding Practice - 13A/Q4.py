s = int(input())
n = int(input())

for i in range(1,n + 1):
    left_space = " " * (n - i)
    print(left_space, end = "")
    for j in range(0,i):
        print((str(s + j) + " "),end = "")
    print()