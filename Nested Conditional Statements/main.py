condition_a = True
condition_b = True 

if condition_a:
    print("Block 1")
    if condition_b:
        print("Block 2")
    print("Block 3")
print("Block 4")

# greatest among three numbers.
print("Q1. Greatest among three numbers.")

a = int(input("Enter number:"))
b = int(input("Enter number:"))
c = int(input("Enter number:"))

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)

# number divisible by 10 or 5 or neither.
print("number divisible y 10 or 5 or neither")

num = int(input("enter no:"))

if num % 10 == 0:
    print("divisible by 10")
elif num % 5 == 0:
    print("divisble by 5")
else:
    print("not divisble")
    
