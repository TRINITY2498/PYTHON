s = input()

for ch in s:
    
    if ch == " ":
        continue
    
    else:
        
        row = ord(ch) - 1 
    
        print(chr(row))