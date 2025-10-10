a = input()
len_of_a = len(a)
b = ""
for i in range(0, len_of_a):
    if i == 0:
        b = b + a[i]  
    else:
        b = b + "-" + a[i]
print(b)
