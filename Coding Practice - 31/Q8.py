# Rename Key.

fruits = {
    "apples": 10,
    "bananas": 20,
    "mangoes": 15,
    "oranges": 200,
    "watermelons": 50
}

key1 = input()
key2 = input()

dict_a = {}

for key, value in fruits.items():
    
    if key == key1:
        
        dict_a[key2] = value
    
    else:
        
        dict_a[key] = value 
        
print(list(dict_a.items()))