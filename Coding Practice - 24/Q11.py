s = input()
digit = []

for ch in s:
    
    if ch.isdigit():
        
        digit += [int(ch)]

print(sum(digit))
print(min(digit))
print(max(digit))

        
    