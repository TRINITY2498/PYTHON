s = input().split(",")
lis = []

for i in s:
    
    lis += [int(i)]

sorted_list = sorted(lis)

if len(sorted_list) % 2 == 0:
    
    first_digit = sorted_list[(len(sorted_list) // 2) - 1]
    second_digit = sorted_list[len(sorted_list) // 2]
    
    result = (first_digit + second_digit) / 2
    
else:
    
    result = sorted_list[(len(sorted_list) // 2)]
    

print(result)
    
 
