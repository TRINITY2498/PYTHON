n = int(input())

group_1 = n in [1,7,13,19,25]
group_2 = n in [2,8,14,20,26]
group_3 = n in [3,9,15,21,27]
group_4 = n in [4,10,16,22,28]
group_5 = n in [5,11,17,23,29]
group_6 = n in [6,12,18,24,30]

if group_1:
    print("Group 1")
elif group_2:
    print("Group 2")
elif group_3:
    print("Group 3")
elif group_4:
    print("Group 4")
elif group_5:
    print("Group 5")
elif group_6:
    print("Group 6")