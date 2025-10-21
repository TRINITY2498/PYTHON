m = int(input())
n = int(input())
digit = 0
x = 0

for i in range(m,n + 1):
    digit = n - x
    if digit % 2 != 0:
        print(digit,end = " ")
    x = x + 1