s = input().split(",")

lis = []

for i in s:
    
    lis += [int(i)]

list_x = sorted(lis)

print(list_x)