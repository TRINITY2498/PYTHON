def get_digits(str_1):
    
    digit_list = []
    
    for digit in str_1:
        
        if digit.isdigit():
            
            digit_list += [int(digit)]
    
    return digit_list

s = input()

row = get_digits(s)

sum_of = sum(row)
smallest = min(row)
largest = max(row)

print(sum_of)
print(smallest)
print(largest)
