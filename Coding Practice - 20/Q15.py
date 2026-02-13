n = int(input())
row = []

for i in range(n):
    
    char = input()
    
    row = row + [char]

for j in range((len(row) - 1),-1,-1 ):
    
    print(row[j])