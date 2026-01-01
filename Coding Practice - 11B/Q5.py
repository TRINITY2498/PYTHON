p = input()

count = 0

for i in p:
    is_digit = i.isdigit()
    if is_digit:
        count = count + 1
        
if count >= 1:
    print("Valid Password")
else:
    print("Invalid Password")