def get_odd_numbers_in_range(start_number, end_number):
    
    for i in range(start_number, end_number + 1):
        
        if i % 2 != 0:
            
            print(i,end = " ")
    

start_number = int(input())
end_number = int(input())

get_odd_numbers_in_range(start_number, end_number)