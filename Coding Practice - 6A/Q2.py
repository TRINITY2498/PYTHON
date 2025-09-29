a = input()
m = input()
a_per = int(a[0 : len(a) - 1])

result = ((a_per >= 75) or (m == "Y"))

if result:
    print("Allowed to write exam")
else:
    print("Cannot write exam")