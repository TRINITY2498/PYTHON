s = input().split(",")

lis = []

count = 0
sum_of = 0

for i in s:
    
    lis += [int(i)]
    
list_x = sorted(lis, reverse = True)

for j in list_x:
    
    if count < 5:
        
        sum_of += j 
        
        count += 1

print(sum_of)