s = input()
first_char = s[0]
row = s[0].lower()

for ch in s[1: ]:
    
    if ch == ch.upper() and ch.isalpha():
        
        row = row + "_" + ch.lower()
    
    else:
        row = row + ch 

print(row)