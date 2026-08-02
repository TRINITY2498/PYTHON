# Adding Key Value Pair.

dict_a = { "name" : "Kaustubh", "age" : 23}

dict_a['city'] = 'Goa'

dict_a['age'] = 24

print(dict_a)

# Modifying an Existing Item.

dict_a['age'] = 24

print(dict_a)

# Deleting an Existing Item.

del dict_a['age']

print(dict_a)

# Getting Keys.

print(dict_a.keys())

for key in dict_a.keys():
    
    print(key)

# Getting Values.


print(dict_a.values())

for value in dict_a.values():
    
    print(value)


# Getting Items.

print(dict_a.items())

for item in dict_a.items():
    
    print(item)

# ---------

for key, value in dict_a.items():
    
    pair = "{} {}".format(key, value)
    
    print(pair)


#---------

view = dict_a.keys()

print(view)

dict_a['roll_no'] = 10

print(view)

# Converting to Dictionary.

list_a = [ ("name", "Teja"), ["age", 15], ("roll_no",15)]

dict_a = dict(list_a)

print(dict_a)