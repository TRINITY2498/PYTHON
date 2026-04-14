s = input().split(",")

nums = []

for x in s:
    
    nums.append(x)

max_count = 0
mode = nums[0]

for num in nums:
    
    count = nums.count(num)
    
    if count > max_count:
        
        max_count = count
        mode = num
    
print(mode)