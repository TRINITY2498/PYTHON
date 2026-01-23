m = int(input())
n = int(input())
even_count = 0 
odd_count = 0 

for i in range(m,n + 1):
    
    if i < 0:
        i = i * (-1)
    
    if i % 2 == 0:
        even_count = even_count + 1 
    
    else:
        odd_count = odd_count + 1 

print(odd_count)
print(even_count)