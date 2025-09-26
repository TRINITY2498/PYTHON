n = int(input())

check_div = n % 3 == 0

if check_div:
    print(n * 3)
else:
    print(n * 2)