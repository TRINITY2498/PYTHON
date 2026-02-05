w = input()

w_len = len(w)
count = 0 
row = ""

for ch in w:
    
    if count == w_len - 1:
        row = row + ch 
    
    else:
        row = row + ch + "-"
        count = count + 1

print(row)
    