nums = input().split(",")
k = int(input())

int_set = set()

for num in nums:
    
    digit = int(num)
    
    int_set.add(digit)


for current in sorted(int_set):
    
    required = k - current 
    
    if required in int_set and current < required:
         
        pair = tuple(sorted((current,required)))
        
        print(pair)
        