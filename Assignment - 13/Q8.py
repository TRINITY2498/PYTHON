n = int(input())
k = int(input())

total_num = (k * (k + 1)) // 2 

s = n + (total_num) - 1 

for i in range(1,k + 1):
    for j in range(1,i + 1):
        print(str(s) + " ",end = "")
        s = s - 1
    print()