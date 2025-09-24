a = input()
b = input()

a_last_three = len(a) - 3 
b_last_three = len(b) - 3

print(a[a_last_three : ] == b[b_last_three : ])