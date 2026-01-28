s = input()
valid = True 

for ch in s:
    
    if ch.isalpha() or ch.startswith("_"):
        valid = True 
    
    else:
        valid = False 
        break 

if valid:
    
    print("True")

else:
    
    print("False")
    