x = int(input())
n = int(input())
counter = 1
num = 0
prod = 1 

while counter <= n: 
    num = x + counter 
    counter = counter + 1
    prod = prod * num 
print(prod)