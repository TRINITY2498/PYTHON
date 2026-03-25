s = input().split(",")
lis = []

for i in s:
    
    lis += [int(i)]

sum_of_lis = sum(lis)

mean = sum_of_lis / len(lis)

print(mean)
    