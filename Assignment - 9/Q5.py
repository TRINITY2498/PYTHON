n = int(input())
j = n

for i in range(1,n + 1):
    print("* " * i)

for i in range(0,n + 2):
    print("* " * (n - i))