def calculate_power(x, y):
    
    if y == 0:
        
        return 1 
    
    else:
        
        return x * calculate_power(x,y - 1)


a = int(input())
b = int(input())

result = calculate_power(a,b)

print(result)
