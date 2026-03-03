"""
def greet(arg1, arg2):
    print(arg1 + " " + arg2)
    
greeting = input()
name = input()

greet(greeting,name)

"""
"""
# Default Arguements :-

def greet(arg1 = "Hi", arg2 = "Ram"):
    print(arg1 + " " + arg2)
    
greeting = input()
name = input()

greet()
greet("Hello")
greet("Hello", "Teja")
greet(arg2 = "Teja")

"""

"""
# Passing Immutable Objects :-

def increment(a):
    
    a += 1
    
a = int(input())

increment(a)
print(a)

"""