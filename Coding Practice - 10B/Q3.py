s = input()
count = 0 

for i in s:
    if i in ("aeiou"):
        count = count + 1
if count > 2:
    print("String has more than two vowels")
elif count <= 2:
    print("String doesn't have more than two vowels")