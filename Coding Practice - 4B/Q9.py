n = int(input())

triple = n * 3

div_by_6 = triple % 6 == 0

if div_by_6:
    print(triple)
else:
    print(n)