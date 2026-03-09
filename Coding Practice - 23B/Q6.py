def get_even_numbers_count(numbers):
    
    numbers = numbers.split()
    
    count = 0 
    
    for i in numbers:
        
        i = int(i)
        
        if i % 2 == 0:
            
            count = count + 1 
    
    return count 

numbers = input()
result = get_even_numbers_count(numbers)
print(result)