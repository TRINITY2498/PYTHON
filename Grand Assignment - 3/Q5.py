s = input().split()

freq = {}

for word in s:
    
    if word in freq:
        
        freq[word] += 1 
    
    else:
        
        freq[word] = 1 
    
for word, count in freq.items():
    
    print("{}: {}".format(word, count))