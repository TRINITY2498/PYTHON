str_a = input()
a = str_a.split(",")
i = 0
for item in a:
    a[i] = int(item)
    i += 1

tup_a = tuple(a)
print(tup_a)
