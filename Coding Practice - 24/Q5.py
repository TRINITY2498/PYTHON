s = input().split(",")
n = int(input())
lis = []
len_s = len(s)

for i in range(n, len_s):
    
    lis += [int(s[i])]
    
print(max(lis))