a = input()
b = input()

result = "No overlapping"

for i in range(len(a)):
    
    suffix = a[i : ]
    
    if b.startswith(suffix):
        
        result = suffix
        
        break 

print(result)