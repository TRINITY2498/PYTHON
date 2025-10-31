m = int(input())
n = int(input())
count_1 = 0 

for i in range(m,n + 1):
    count_1 = count_1 + len(str(i))
print(count_1)
