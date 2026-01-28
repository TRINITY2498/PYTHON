s = input()

word = s.split()

smallest = word[0]

for w in word:
    
    if w.lower() < smallest.lower():
        
        smallest = w 

print(smallest)