s = input()

row = ""

words = s.split()

len_words = len(words)

reverse_words = words[len_words - 1 : : -1]

for word in reverse_words:
    
    row = row + word + " "

print(row.strip())
    