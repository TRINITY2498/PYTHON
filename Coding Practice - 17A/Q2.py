s = input()
n = int(input())
count = 0

for ch in s:
    
    uni_value = ord(ch)
    
    if uni_value == n:
        count = count + 1 
print(count)