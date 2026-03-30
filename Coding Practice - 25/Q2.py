def get_sum(numbers):

    

    if len(numbers) == 0:

        

        return 0 

    

    else:

        

        return int(numbers[0]) + get_sum(numbers[1 : ])

numbers = input().split()

sum_of_numbers = get_sum(numbers)

print(sum_of_numbers)
