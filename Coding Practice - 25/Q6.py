def sum_of_the_digits(number):
    
    number = str(number)
    
    n = len(number)
    
    if n == 0: 
        
        return 0 
    
    else:
        
        return int(number[0]) + sum_of_the_digits(number[1 : ])
    


number = int(input())

result = sum_of_the_digits(number)

print(result)
