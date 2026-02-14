L = [1, "two", 9, 5.09, "Three", -558, "four", -93.7, "six"]

l1 = int(input())
l2 = int(input())

temp = L[l1]

L[l1] = L[l2]

L[l2] = temp 

print(L)

