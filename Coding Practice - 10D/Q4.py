n = int(input())

plus_count = 0 

for i in range(1,n + 1):
    space = ((2 * n) - (2 * i))
    row = ((" " * space) + ("+ " * plus_count) + "#")
    plus_count = plus_count + 1 
    print(row)
    
new_plus_count = plus_count - 2
    
for i in range(1,n):
    space = (2 * i)
    row = ((" " * space) + ("+ " * new_plus_count) + "#")
    new_plus_count = new_plus_count - 1 
    print(row)