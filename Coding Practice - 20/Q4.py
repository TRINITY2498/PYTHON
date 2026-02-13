L = ["5", "eat", "9.80", "Water", "python", "-678", "7685.26", "-2.5", "sing"]

# Write your code here

s = input()
found_ch = True

for ch in L: 
    
    if s == ch:
        found_ch = True
        break
    
    else:
        found_ch = False 

if found_ch:
    
    print("True")

else:
    
    print("False")