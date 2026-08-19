# Student ID Map.

names = input().split(",")
stud_id = input().split(",")

dict_a = {}

for i in range(len(names)):
    
    dict_a[names[i]] = stud_id[i]


for key, value in sorted(dict_a.items()):
    
    pair = "{} {}".format(key, value)
    
    print(pair)
    
    
