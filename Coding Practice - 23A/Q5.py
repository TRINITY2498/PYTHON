def compare_numbers(first_number, second_number):
    
    if((first_number > 100 and second_number > 100) and (first_number < second_number)):
        
        print("True")
    
    else:
        
        print("False")
    

first_number = int(input())
second_number = int(input())

compare_numbers(first_number,second_number)