s = input()
dash = "-"
result = ""

for i in range(len(s)):
    if s[i].isupper():
        result = result + dash + (s[i].lower())
    else:
        result = result + s[i]
print(result)