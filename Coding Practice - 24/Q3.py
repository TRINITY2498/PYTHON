s = input().split(",")
lis = []

for i in s:
    
    lis += [int(i)]
    
smallest = min(lis)

print(smallest)