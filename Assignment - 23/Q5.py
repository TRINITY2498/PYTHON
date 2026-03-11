def number_of_cars_needed(no_of_people):
    
    result = (no_of_people + 4) // 5
    
    return result


no_of_people = int(input())

print(number_of_cars_needed(no_of_people))
