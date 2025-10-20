m = int(input())
n = int(input())
sum = 1

for i in range(m,n + 1):
    if i % 2 != 0:
        sum = sum * i 
print(sum)