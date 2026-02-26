def show_numbers(number):
    
    for i in range(number + 1):
        
        if i % 2 == 0:
            
            print(i,"EVEN")
        
        else:
            print(i,"ODD")


number = int(input())

show_numbers(number)
