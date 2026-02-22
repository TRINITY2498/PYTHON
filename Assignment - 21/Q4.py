s = input()
numbers = s.split()
sum_of_numbers = 0 
len_numbers = len(numbers)


for number in numbers:
    
    number = int(number)
    
    sum_of_numbers = sum_of_numbers + number 


avg_of_numbers = sum_of_numbers / len_numbers 

print(round(avg_of_numbers,2))
