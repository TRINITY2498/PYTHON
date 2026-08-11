def more_args(*args):
    
    print(args)
    

more_args(1,2,3,4,5,6)
more_args(20,30,40,50,60)
more_args()


# ------------------------------------

def greet(arg1 = "Hi", arg2 = "Ram"):
    
    print(arg1 + " " + arg2)
    
data = ["Hello", "Teja"]

greet(*data)


# Keyword Arguements.

def more_args(**kwargs):
    
    print(kwargs)

more_args(a = 1, b = 2, c = 3)
more_args()


# Iteration.

def more_args(**kwargs):
    
    for i, j in kwargs.items():
        
        print('{} : {}'.format(i, j))

more_args(a = 1, b = 2, c = 3)


# Unpacking Arguements.

def greet(arg1 = "Hi", arg2 = "Ram"):
    
    print(arg1 + " " + arg2)
    

data = {
    
    "arg1" : "Hello",
    "arg2" : "Abhinav"
}

greet(**data)
    