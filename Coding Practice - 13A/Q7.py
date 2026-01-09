n = int(input())

for i in range(1,n + 1):
    original = i 
    num = i 
    temp = i 
    digit_count = 0
    summ = 0
    while temp > 0:
        temp = temp // 10 
        digit_count = digit_count + 1
    
    while num > 0:
        digit = num % 10 
        num = num // 10
        summ = summ + (digit ** digit_count)
        
    if summ == original:
        print(original)

"""

n = int(input())
for num in range(1,n+1):
    digit = str(num)
    power = len(digit)
    total = 0 
    for d in digit:
        total +=int(d)**power 
    if total == num:
        print(num)

"""