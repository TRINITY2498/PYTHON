a = input()

alpha = ""
digit = ""

for item in a:
    
    if item.isalpha():
        
        alpha += item 
    
    elif item.isdigit():
        
        digit += item

print(alpha + digit)