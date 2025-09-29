n = input()

len_n = len(n)

if len_n == 1:
    print(n)
elif len_n == 2:
    sum = int(n[0]) + int(n[1])
    print(sum)
elif len_n == 3:
    sum = int(n[0]) + int(n[1]) + int(n[2])
    print(sum)
elif len_n == 4:
    sum = int(n[0]) + int(n[1]) + int(n[2]) + int(n[3])
    print(sum)