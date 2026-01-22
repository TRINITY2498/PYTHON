"""

for i in range(10):
    
    if i == 2:
        break 
    print(i)
print("End")

"""
"""

i = 0 

while i < 10:
    
    if i == 2:
        break 
    print(i)
    i = i + 1 
print("End")

"""
"""

for a in range(2):
    
    print("Outer :" + str(a))
    
    for b in range(4):
        
        if b == 1:
            break 
        
        print("  inner :" + str(b))

"""

"""
for a in range(3):
    
    if a == 1:
        
        continue 
    print(a)
print("End")

"""

"""

age = int(input())
output = ""

if age >= 20:
    pass
elif  age > 12:
    pass
else:
    pass
print(output)

"""