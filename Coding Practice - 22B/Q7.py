def get_weather_report(temperature):
    
    if temperature < 22:
        
        return "Cold"
    
    elif temperature >= 22 and temperature < 35:
        
        return "Warm"
    
    else:
        
        return "Hot"


temperature = int(input())

result = get_weather_report(temperature)

print(result)
