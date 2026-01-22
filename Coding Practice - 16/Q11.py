s = input()
row = ""

for ch in s:
    
    if ch in ("AEIOUaeiou"):
        
        continue 
    
    else:
        row = row + ch

print(row)