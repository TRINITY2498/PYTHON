s = input()
s = s.split()
lis = []

for i in s:
    
    lis += [int(i)] 
    
    sum_of = sum(lis)

print(sum_of)