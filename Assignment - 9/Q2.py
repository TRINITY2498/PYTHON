n = int(input())
k = int(input())
pos = 0

for i in range(1,n + 1):
    pos = pos + (i ** k)
print(pos)