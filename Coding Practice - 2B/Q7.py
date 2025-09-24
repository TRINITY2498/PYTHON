a = input()
b = input()
i = int(input())

check_part = a[i : len(b) + i]

print(check_part == b)