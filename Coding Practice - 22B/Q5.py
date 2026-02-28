def valid_string(string):
    
    first_char = string[0]
    
    if len(string) >= 6 or first_char.isdigit():
        
        return "Valid String"
    
    else:
        
        return "Invalid String"
    



string = input()

result = valid_string(string)

print(result)