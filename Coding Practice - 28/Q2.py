def extract_elements(nums):
    
    int_list = []
    
    for num in nums:
        
        if(num.isdigit()):
            
            digit = int(num)
            
            int_list.append(digit)
        
        else:
            
            continue
    
    int_list.sort()
    
    print(int_list)

nums = input().split(",")

extract_elements(nums)


