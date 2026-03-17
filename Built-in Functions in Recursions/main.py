"""
def add_item(list_x):
    
    list_x += [3]

list_a = [1,2]
add_item(list_a)
print(list_a)

"""

"""
def add_item(list_x):
    
    list_x = list_x + [3]
    print(list_x)

list_a = [1,2]
print(list_a)
add_item(list_a)
print(list_a)

"""
"""
# Passing Mutable Objects

def add_item(list_x = []):
    
    list_x += [3]
    print(list_x)

add_item()
add_item([1,2])
add_item()

"""

# Built-in Functions:-

"""
smallest = min(3,4,2,1,7)

print(smallest)

"""

"""
smallest = min("Python","Java")

print(smallest)

"""

"""
largest = max([-3,4,1,2,7])

print(largest)

"""

"""
sum_of = sum([-3,4,1,2,7])

print(sum_of)

"""

"""
list_a = [3,5,2,1,4,6]
list_x = sorted(list_a)

print(list_x)

"""

"""
list_a = [3,5,2,1,4,6]
list_x = sorted(list_a, reverse = True)

print(list_x)

"""