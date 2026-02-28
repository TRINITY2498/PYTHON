def calculate_percentage(number):
    
    if number < 1000:
        
        perc = (5 / 100) * number
    
    else:
        
        perc = (10 / 100) * number
    
    
    return perc 
 


number = int(input())

result = calculate_percentage(number)

print(result)