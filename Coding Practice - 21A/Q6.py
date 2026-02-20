n = input()
n_split = n.split()
smallest = n_split[0]
smallest = int(smallest)

for i in n_split:
    
    i = int(i)
    
    if smallest >= i:
        
        smallest = i 
    
    elif smallest < i:
        
        continue

print(smallest)