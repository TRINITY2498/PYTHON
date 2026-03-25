s = input().split(",")
n = int(input())
lis = []

for i in s:
    
    lis += [int(i)]

sorted_list = sorted(lis)

print(sum(sorted_list[ : n]))