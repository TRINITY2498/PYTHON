def get_first_upper_letter(string):
    
    for ch in string:
        
        if ch.isupper():
            
            return ch 
            break


string = input()
upper_case_character = get_first_upper_letter(string)
print(upper_case_character)