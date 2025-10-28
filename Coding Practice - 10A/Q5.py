n = input()
k = len(n)
arm = 0

for i in n:
    arm = arm + (int(i) ** k)
if (arm == int(n)):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")