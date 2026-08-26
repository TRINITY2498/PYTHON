# Numbers in String - 1.

s = input()

numbers = []

current_num = ""

for i in s:
    
    if i.isdigit():
        
        current_num += i 
    
    else:
        
        if current_num:
            
            numbers.append(int(current_num))
        
        current_num = ""
    
if current_num:
    
    numbers.append(int(current_num))

sum_of_nums = sum(numbers)
average = round(sum_of_nums / len(numbers), 2)

print(sum_of_nums)
print(average)