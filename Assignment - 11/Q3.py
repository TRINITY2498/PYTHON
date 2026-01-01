s = input()

vowels = "aeiouAEIOU"
results = ""

for ch in s:
    if ch not in vowels:
        results = results + ch
print(results)