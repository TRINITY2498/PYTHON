s = input()

n = len(s)
result = ""

for i in range(1,n):
    if s[i].isupper():
        result = result + "-" + s[i]
    else:
        result = result + s[i]
result = s[0] + result
print(result.lower())
    