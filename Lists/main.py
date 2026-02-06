"""

a = 2 

list_a = [5, "Six", a, 8.2]

list_b = [1, list_a]

print(list_b)

print(len(list_a))

print(list_a[1])

for item in list_a:
    
    print(item)

list_c = list_a + list_b 

print(list_c)

list_d = ["a", "b", "c"]

list_c = list_a + list_d

print(list_c)

"""
"""

list_e = []

print(list_e)

for i in range(1,4):
    list_e += [i]
print(list_e)


list_f = [1,2]

list_g = list_f * 2 

print(list_g)

print(list_a[ : 2])

print(list_a[0,5,3])

"""

color = "red"
list_x = list(color)
print(list_x)

list_a = list(range(4))

print(list_a)

list_a[2] = 4 
print(list_a)