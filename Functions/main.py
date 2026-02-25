"""

def greet():
    
    print("Hello")
    
name = input()
greet()
print(name)

"""

"""

def greet(word):
    
    msg = "Hello " + word
    
    print(msg)
    
name = input()

greet(word = name)

"""

"""

def greet(word):
    
    msg = "Hello " + word
    
    return msg
    
name = input()

greeting = greet(word = name)

print(greeting)

"""