x = int(input())
n = int(input())
digit = 2 
neg = 1 
sor = 0

for i in range(n):
    ser = ((x ** digit) * neg)
    sor = sor + ser
    neg = neg * (-1)
    digit = digit + 2
print(sor)
    