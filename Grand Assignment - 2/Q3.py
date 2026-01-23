s = input()
count_g = 0 
count_r = 0

for i in s:
    
    if i == "G":
        count_g = count_g + 1
    
    elif i == "R":
        count_r = count_r + 1 

if count_g > count_r:
    print(count_r)

else:
    print(count_g)