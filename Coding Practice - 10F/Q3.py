n = int(input())

for i in range(1,n + 1):
    if i == 1:
        row = ((str(i)))
    else:
        left = str(i)
        mid =  (2 * i) - 3
        row = (left + (" ") * mid + str(i))

    print(row)

for i in range(1,n):
    digit = n - i
    if i == (n - 1):
        row = (str(digit))
    else:
        left = str(digit)
        mid_two = 2 * (n - i) - 3
        row = (left + (" ") * mid_two + (str(digit)))
    
    print(row)