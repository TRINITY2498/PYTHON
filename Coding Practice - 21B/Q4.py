s = input()
row = ""

s_split = s.split()

for word in s_split:
    
    reverse = (word[ : : -1]) + " "
    
    row = row + reverse

print(row.strip())

    
    