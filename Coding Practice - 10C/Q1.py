x = int(input())
n = int(input())
sor = 0
digit = 1

for i in range(n):
    ser = (x ** digit)
    sor = sor + ser 
    digit = digit + 2 
print(sor)