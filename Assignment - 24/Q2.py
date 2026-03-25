s = input().split(",")
n = int(input())
lis = []

for i in s:
    
    lis += [int(i)]

sorted_list = sorted(lis)

result = sorted_list[n - 1]

print(result)