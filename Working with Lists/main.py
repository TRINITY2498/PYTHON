"""

animal = ['Cat', 'dog']
wild_animals = ['Tiger', 'Fox']

animal += [wild_animals]

print(animal)

"""
"""

print(id("Hello"))

"""

"""

a = "Hello"
print(id(a))
a = a + " World"
print(id(a))

"""

"""
list_a = [1,2,3]

print(id(1))
print(id(2))
print(id(3))
print(id(list_a))

"""

"""

list_a = [1,2,3]
list_b = [1,2,3]

print(id(list_a))
print(id(list_b))

"""

"""

list_a = [1,2,3,5]
list_b = list_a
list_b[3] = 4
print("list a : " + str(list_a))
print("list b : " + str(list_b))

"""

"""

list_a = [1,2]
list_b = list_a
list_a = [6,7]
print("list a : " + str(list_a))
print("list b : " + str(list_b))

"""
"""

list_a = [1,2]
list_b = list_a
list_a = list_a + [6,7]
print("list a : " + str(list_a))
print("list b : " + str(list_b))

"""

"""

list_a = [1,2]
list_b = [3, list_a]
list_a[1] = 4 
print(list_a)
print(list_b)

""" 

"""

a = 2
list_a = [1,a]

print(list_a)

a = 3 
print(list_a)

"""