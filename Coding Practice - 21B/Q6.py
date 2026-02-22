s = input()
lis = []

numbers = s.split()

len_numbers = len(numbers)

if len_numbers % 2 != 0:
    
    len_numbers = (len_numbers + 1) // 2

else:
    
    len_numbers = len_numbers // 2
    
for i in range(len_numbers):
    
    num = int(numbers[i])
    
    lis = lis + [num]

print(lis)