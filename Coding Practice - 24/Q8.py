s = input().split(",")

lis = []

for i in s:
    
    lis += [int(i)]

list_x = sorted(lis, reverse = True)

print(list_x[1])