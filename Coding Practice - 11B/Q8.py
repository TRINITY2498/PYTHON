s = input()
count = 0

for ch in s:
    if ch.isupper():
        count = count + 1 

if count >= 1:
    print("Valid Password")
else:
    print("Invalid Password")