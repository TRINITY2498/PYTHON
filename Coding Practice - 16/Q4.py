s = input()
index = 0 
first_word = ""

for ch in s:
    
    if ch == " ":
        break 
    else:
        index = index + 1
    
    first_word = first_word + ch 
    
first_word = first_word.upper()

print(first_word + s[index : ])