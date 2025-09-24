w = input()
n = int(input())

first_part = w[ : n]
last_part = w[len(w) - n : ]

print(first_part != last_part)