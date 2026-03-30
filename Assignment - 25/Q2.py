def get_index(numbers_list, number):
     
    if int(numbers_list[0]) == number:
        
        return 0
    
    else:
        
        return 1 + get_index(numbers_list[1 : ],number)
        
    


numbers_list = input().split()
number = int(input())


number_index = get_index(numbers_list, number)

print(number_index)