s = input().split(",")
n = int(input())

lis = []

for i in s:
    
    lis += [int(i)]

lis_x = sorted(lis, reverse = True)

print(lis_x[n - 1])

    
    