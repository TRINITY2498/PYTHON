def get_sum_of_squares(numbers):
    
    if numbers == []:
        
        return 0 
    
    else:
        
        return int(numbers[0]) ** 2 + get_sum_of_squares(numbers[1 : ])
        



    
numbers = input().split()

squares_sum = get_sum_of_squares(numbers)
print(squares_sum)
