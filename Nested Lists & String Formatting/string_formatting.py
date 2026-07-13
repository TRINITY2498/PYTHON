'''

name = input()
age = int(input())
msg = ("Hi " + name + ". You are " + str(age) + " years old.")

print(msg)

'''

'''

name = input()
age = int(input())
msg = ("Hi {}. You are {} years old.")

print(msg.format(name, age))

'''