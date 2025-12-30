s = input()

for ch in s:
    is_upper = ch.isupper()
    
    if is_upper:
        print(ch,end = "")