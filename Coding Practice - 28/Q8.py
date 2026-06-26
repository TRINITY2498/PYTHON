list_a = [5, 20, 3, 7, 6, 8]
k = int(input())
list_len = len(list_a)
list_a.sort(reverse = True)
res = (list_a[0 : k])
res.sort()

for i in range(k):
    res[i] = str(res[i])
print(" ".join(res))
