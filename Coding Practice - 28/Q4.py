def set_relation(nums):
    
    int_list = []
    
    for num in nums:
        digit = int(num)
        
        int_list.append(digit)
    
    set_num = set(int_list)
    
    is_superset = num_set.issuperset(set_num)
    is_subset = num_set.issubset(set_num)
    is_disjoint = num_set.isdisjoint(set_num)
    
    
    if is_superset:
        
        print("Superset")
    
    elif is_subset:
        
        print("Subset")
    
    elif is_disjoint:
        
        print("Disjoint Set")
        


num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

nums = input().split()

set_relation(nums)
