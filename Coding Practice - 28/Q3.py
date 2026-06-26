def missing_numbers(nums):
    
    int_list = []
    
    for num in nums:
        
        int_list.append(int(num))
    
    nums_set = set(int_list)
    
    max_nums = max(int_list)
    
    missing_list = []
    
    for i in range(1, max_nums + 1):
        
        if i not in nums_set:
            
            missing_list.append(i)
    
    missing_list.sort()
    
    print(missing_list)
    




nums = input().split()

missing_numbers(nums)