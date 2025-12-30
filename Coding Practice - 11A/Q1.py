s = input()


for i in s:
    is_alpha = i.isalpha()
    
    if is_alpha:
        print(i, end = "")