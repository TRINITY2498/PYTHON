n = int(input())
count = 0

for i in range(1,n + 1):
    for j in range(1,n + 1):
        for k in range(1,n + 1):
            if (i < j < k) and ((i ** 2) + (j ** 2) == (k ** 2)):
                count = count + 1
print(count)