# Combine Two Dictionaries. 

key1 = input().split()
value1 = input().split()

key2 = input().split()
value2 = input().split()

dict_a = {}

for i in range(len(key1)):
    
    dict_a[key1[i]] = int(value1[i])
    

for j in range(len(key2)):
    
    dict_a[key2[j]] = int(value2[j])
    

print(list(sorted(dict_a.items())))