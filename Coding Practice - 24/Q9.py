s = input().split(",")
lis = []

for i in s:
    
    lis += [int(i)]

largest = max(lis)

smallest = min(lis)

diff = largest - smallest 

print(diff)

    
    