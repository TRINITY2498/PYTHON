n = int(input())
small = int(input())

for i in range(n - 1):
    a = int(input())
    if a < small:
        small = a
print(small)