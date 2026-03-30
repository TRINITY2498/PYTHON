def get_largest_square(numbers):
    
    if numbers == []:
        
        return 0
    
    else:
        
        return max(int(numbers[0]) ** 2, get_largest_square(numbers[1 : ]))


numbers = input().split()

result = get_largest_square(numbers)
print(result)