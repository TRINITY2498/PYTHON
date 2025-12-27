n = int(input())

for i in range(1,n + 1):
    left_space = (n - i) * 2
    hollow_space = (2 * i - 3)
    if i == 1:
        row = (" " * left_space) + (str(i))
    else:
        row = (" " * left_space + (str(i)) + (" " * hollow_space) + (str(i)))
        k = n - 1
    print(row)

for i in range (1,n):
    left_space = 2 * i
    hollow_space = (2 * k) - 3
    if i == (n - 1):
        row = (" " * left_space) + (str(n - i)) 
    else:
        row = (" " * left_space + (str(n - i)) + (" " * hollow_space) + str(n - i))
        k = k - 1
    print(row)
        