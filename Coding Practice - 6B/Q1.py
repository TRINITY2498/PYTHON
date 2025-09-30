n = int(input())

group_1 = ((n == 1) or (n == 3) or (n == 5) or (n == 7) or (n == 9))
group_2 = ((n == 2) or (n == 4) or (n == 6) or (n == 8) or (n == 10))

if group_1:
    print("Group A")
elif group_2:
    print("Group B")