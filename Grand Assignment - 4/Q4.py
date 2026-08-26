# Numbers in String - 1.

s = input()

total = 0 
count = 0

for i in s:
    
    if i.isdigit():
        
        total += int(i)
        
        count += 1
    
average = total / count 

print(total)
print(round(average, 2))