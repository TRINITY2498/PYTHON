s = input()
smallest = s[0]

for ch in s: 
    
    if ord(ch) < ord(smallest):
        smallest = ch 
print(smallest)
        
        