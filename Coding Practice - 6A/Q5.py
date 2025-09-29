s = input()

num = int(s[0 : len(s) - 1])
last_char = s[-1]

if last_char == "T":
    result = num * 10
    print(result)
elif last_char == "H":
    result = num * 100
    print(result)
elif last_char == "K":
    result = num * 1000
    print(result)