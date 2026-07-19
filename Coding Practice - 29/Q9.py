s = input().split()

# converting list to string 

list_string = ""

for item in s:
    
    list_string += item 

list_string = list_string.lower()

list_string_set = set(list_string)

for char in sorted(list_string_set):
    
    frequency = list_string.count(char)
    
    print(char + ": " + str(frequency))
    
    
    