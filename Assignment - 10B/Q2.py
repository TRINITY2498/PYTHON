n = int(input())

for i in range(1,n + 1):
    if i == 1:
        mid_space = (n - i) * 4
        row = ("* " + " " * mid_space + "*")
    elif i == n:
        row = ("* ") * (2 * n)
    else:
        mid_space = (n - i) * 4
        hollow_space = (2 * i) - 4
        row = ("* " + " " * hollow_space + "* " + " " * mid_space + "* " + " " * hollow_space + "*")
    print(row)