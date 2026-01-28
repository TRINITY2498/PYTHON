s = input()

word = s.split()

smallest = word[0]
largest = word[0]

for w in word:
    
    if w.lower() < smallest.lower():
        smallest = w
    
    elif w.lower() > largest.lower():
        largest = w 
        
print(smallest,end = " ")
print(largest)