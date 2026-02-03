T = input()

# finding the last character 

last_char = len(T) - 1 
digit = int(T[0 : len(T) - 1])

# Checikng M or S 

if T[last_char] == "M":
    
    hour = digit / 60 
    
    round_hour = round(hour,2)
    
    print(str(round_hour) + "H")
    

elif T[last_char] == "S":
    
    hour = digit / 3600
    
    round_hour = round(hour,2)

    print(str(round_hour) + "H")    
    