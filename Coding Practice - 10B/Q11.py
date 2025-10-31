x = input()
n = int(input())
sor = 0 

for i in range(1,n + 1):
    ser = x * i 
    ser_sqr = (int(ser) ** 2)
    sor = sor + ser_sqr
print(sor)
    