a = int(input())
b = int(input())
c = int(input())

is_between = ((a > 9 and a < 21) or (b > 9 and b < 21) or (c > 9 and c < 21))

if is_between:
    print("True")
else:
    print("False")