a = int(input())
s = input()

b_w = (a > 12 and a < 60)
equals_to = (s == "yes" or s == "no")

print(b_w or (s == "yes"))