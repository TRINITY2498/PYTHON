n = int(input())
digit = 2
sor = 0

for i in range(1,n + 1):
    ser = str(digit) * i 
    sor = int(ser) + sor

print(sor)
