s = input()
space = " "

for i in range(len(s)):
    
    if i == 0:
        result = s[i]
        
    elif s[i].isupper():
        result = result + space + s[i]
    else: 
        result = result + s[i]
    
print(result)
    