s = input()
numbers = s.split()
largest = int(numbers[0])

for number in numbers:
    
    number = int(number)
    
    if largest <= number:
        
        largest = number
    

print(largest)