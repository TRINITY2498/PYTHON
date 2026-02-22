s = input()
s = s.lower()

words = s.split()

for word in words:
    
    len_word = len(word)
    
    first_char = word[0]
    last_char = word[-1]
    
    if first_char == last_char:
        
        print("True")
    
    else:
        print("False")
            
            