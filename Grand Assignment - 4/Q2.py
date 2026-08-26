# Ordered Matrix.

def convert_str_to_int(list_a):
    
    new_list = []
    
    for item in list_a:
        
        num = int(item)
        
        new_list.append(num)
    
    return new_list 
    
m, n = input().split()
m, n = int(m), int(n)

nums_list = []

for i in range(m):
    
    list_a = input().split()
    
    num_list = convert_str_to_int(list_a)
    
    nums_list.extend(num_list)

nums_list.sort()

x = 0 

for row in range(m):
    
    y = ""
    
    for col in range(n):
        
        y += str(nums_list[x])+" "
        x += 1 
    
    print(y)
    