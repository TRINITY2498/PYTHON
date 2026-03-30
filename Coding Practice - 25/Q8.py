def get_reversed_string(string):
    
    n = len(string) - 1
    
    if string == "":
        
        return ""
    
    else:
        
        return get_reversed_string(string[1 :]) + string[0]





string = input()

resultant_string = get_reversed_string(string)
print(resultant_string)