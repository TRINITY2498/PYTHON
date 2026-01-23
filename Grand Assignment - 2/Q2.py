s = input()
v_count = 0 
c_count = 0

for i in s:
    
    if i in ("aeiouAEIOU"):
        v_count = v_count + 1
    
    elif i == " ":
        continue
    
    else:
        c_count = c_count + 1
    
print(v_count)
print(c_count)