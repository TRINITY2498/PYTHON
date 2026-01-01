s1 = input()
s2 = input()

starts_with = s1.startswith(s2)
ends_with = s1.endswith(s2)

if starts_with or ends_with:
    print("True")
else:
    print("False")