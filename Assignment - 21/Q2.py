n = int(input())
s = input()
numbers = s.split()
lis = []

if len(numbers) % 2 != 0:
    
    index = (len(numbers) + 1) // 2

else:
    
    index = len(numbers) // 2
 

for number in numbers:
    
    number = int(number)
    
    lis = lis + [number]

print(lis[index : : ])