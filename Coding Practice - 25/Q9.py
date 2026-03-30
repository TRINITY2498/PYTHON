def get_reversed_string(string):
    
    
    if string == "":
        
        return ""
    
    else:
        
        return get_reversed_string(string[1 :]) + string[0]





string = input()

resultant_string = get_reversed_string(string)
print(resultant_string)