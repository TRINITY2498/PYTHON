s = input().split(",")
n = int(input())
lis = []

for i in s:
    
    lis += [int(i)]
    
new_list = lis[n : ]

print(min(new_list))