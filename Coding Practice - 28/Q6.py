n = int(input())

common_set = set()

for _ in range(n):
    
    
    num = input().split()
    
    if len(common_set) == 0:
        
        common_set = set(num)
    
    else:
        
        common_set = common_set & set(num)

common_list = []

for num in common_set:
    
    digit = int(num)
    
    common_list.append(digit)
    

print(sorted(common_list))
    
    