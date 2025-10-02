d = input()
n = int(input())



day_ahead = (n - 1) % 7 

if d == "Monday":
    day_index = 0
elif d == "Tuesday":
    day_index = 1 
elif d == "Wednesday":
    day_index = 2 
elif d == "Thursday": 
    day_index = 3
elif d == "Friday":
    day_index = 4 
elif d == "Saturday":
    day_index = 5
elif d == "Sunday": 
    day_index = 6
    
result = (day_index + day_ahead) % 7 

if result == 0:
    print("Monday")
elif result == 1:
    print("Tuesday")
elif result == 2:
    print("Wednesday")
elif result == 3:
    print("Thursday")
elif result == 4:
    print("Friday")
elif result == 5:
    print("Saturday")
elif result == 6:
    print("Sunday")