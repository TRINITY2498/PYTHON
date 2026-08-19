# Squares.

sq_dict = {}

n = int(input())

for i in range(1, n + 1):
    
    key = i 
    value = i * i 
    
    sq_dict[key] = value 

print(sq_dict)