s = input().split(",")
lis = []

for i in s:
    
    lis += [int(i)]
    
largest = max(lis)

print(largest)