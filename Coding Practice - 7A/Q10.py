m = int(input())
n = int(input())
counter = 0 
s_m = 0

while counter < n:
    s_m = (counter + m) + s_m
    counter = counter + 1
print(s_m)
