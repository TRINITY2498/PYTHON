c = input()

upper = c.isupper()
lower = c.islower()
digit = c.isdigit()

if upper:
    print("Uppercase Letter")
elif lower:
    print("Lowercase Letter")
elif digit:
    print("Digit")
else:
    print("Special Character")
