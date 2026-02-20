n = input()
n_split = n.split()
lis = []

for i in n_split:
    
    i = int(i)
    
    if i % 3 == 0:
        
        lis = lis + [i]

print(lis)