s1 = input()
s2 = input() 

row = ""

for i in range(len(s1)):
    if i % 2 == 0:
        row = row + s1[i]
    else:
        row = row + s2[i]
    
print(row)