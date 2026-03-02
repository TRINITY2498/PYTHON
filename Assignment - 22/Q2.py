def calculate_bill(amount):
    
    if amount < 500:
        discount = (amount * 5) / 100
        final = amount - discount
    
    elif amount >= 500 and amount < 2500:
        discount = (amount * 10) / 100
        final = amount - discount
    
    else:
        
        discount = (amount * 20) / 100 
        final = amount - discount
        
    return final
        


amount = int(input())

result = calculate_bill(amount)

print(result)
