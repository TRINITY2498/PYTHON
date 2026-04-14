nums_list = [5, 10, 20, 35, 5, 50, 20, 100, 200, 10, 150, 100, 100]

n = int(input())
result = []

for num in nums_list:
    
    if num != n:
        
        result.append(num)
        
print(result)