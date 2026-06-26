def same_elements(nums):
    
    unique = set()
    
    unique_list = []
    
    for i in nums:
        
        num = int(i)
        
        unique.add(num)
    
    for j in unique:
        
        unique_list += [j]
        
    unique_list.sort()
    
    if len(unique_list) == 1: 
        
        print("True")
    
    else:
        
        print(unique_list)



nums = input().split()

same_elements(nums)
