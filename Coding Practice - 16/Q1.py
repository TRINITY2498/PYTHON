s = input()

for ch in s:
    
    if ch == ch.upper() and ch.isalpha():
        break 
print(ch,end = "")