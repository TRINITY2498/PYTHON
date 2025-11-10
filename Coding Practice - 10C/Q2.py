x = int(input())
n = int(input())
sor = 0 
digit = 2

for i in range(n):
    ser = (x ** digit)
    sor = sor + ser 
    digit = digit + 2
print(sor)