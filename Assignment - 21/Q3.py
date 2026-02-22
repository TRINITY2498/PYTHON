s = input()
prod = 1

numbers = s.split()

for number in numbers:
    
    number = int(number)
    
    prod = prod * number

print(prod)