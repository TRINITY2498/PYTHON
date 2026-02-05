s = input()

len_s = len(s)
row = ""

for i in range(0,len_s):
    
    if i == (len_s - 1):
        
        row = row + s[i]
    
    else:
        
        row = row + s[i] + ","

print(row)