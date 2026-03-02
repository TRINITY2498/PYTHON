def validate_atm_pin_code(pin):
    
    if (len(pin) == 4 or len(pin) == 6) and (pin.isdigit()):
        
        return "Valid PIN Code"
        
    else:
        
        return "Invalid PIN Code"

pin = input()

result = validate_atm_pin_code(pin)

print(result)

