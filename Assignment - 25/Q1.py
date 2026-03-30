def get_series_sum(number):
    
    if number == 0:
        
        return 0
    
    else:
        
        return (1 / number) + get_series_sum(number - 1)


number = int(input())

series_sum = get_series_sum(number)

print(round(series_sum,2))

