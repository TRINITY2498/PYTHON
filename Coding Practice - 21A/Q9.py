s = input()
words = s.split()
char = []

for word in words:
    
    if len(word) >= 3:
        char = char + [word[2]]

print(",".join(char))