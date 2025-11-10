n = int(input())

for i in range(1,n + 1):
    spaces = (n - i) * 2
    print(" " * spaces + ("* " * i))