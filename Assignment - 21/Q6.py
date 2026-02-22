s = input()
words = s.split()
row = ""

for word in words:
    
    first_char = word[0]
    
    row = row + first_char
    
print(".".join(row))