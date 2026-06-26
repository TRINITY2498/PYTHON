def common_elements(nums_list1,nums_list2,nums_list3):
    
    int_list1 = []
    int_list2 = []
    int_list3 = []
    
    for num1 in nums_list1:
        
        digit = int(num1)
        
        int_list1.append(digit)
    
    for num2 in nums_list2:
        
        digit = int(num2)
        
        int_list2.append(digit)
    
    for num3 in nums_list3:
        
        digit = int(num3)
        
        int_list3.append(digit)
        
    set_1 = set(int_list1)
    set_2 = set(int_list2)
    set_3 = set(int_list3)
    
    intersection = set_1 & set_2 & set_3
    
    common_list = []
    
    for elements in intersection:
        
        common_list.append(elements)
    
    common_list.sort()
    
    print(common_list)
        
nums_list1 = input().split()
nums_list2 = input().split()
nums_list3 = input().split()

common_elements(nums_list1,nums_list2,nums_list3)