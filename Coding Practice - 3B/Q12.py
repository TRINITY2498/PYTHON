salary = int(input())
experience = int(input())

if (experience < 5):
    print("No Bonus")
elif (experience > 5):
    result = ((5 / 100) * salary)
    print(result)