n = int(input())

r_4 = n % 4
r_5 = n % 5 

if r_4 > r_5:
    print(r_4)
else:
    print(r_5)