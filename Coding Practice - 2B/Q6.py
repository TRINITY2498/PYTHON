a = input()
b = input()
last_part = a[len(a) - len(b) : ] 

print(b == last_part)