u = int(input())

if ((u >= 0) and (u <= 50)):
    cal_u = u * 2
    
elif ((u >= 51) and (u <= 150)):
    cal_u = (50 * 2) + ((u - 50) * 3)
   
elif ((u >= 151) and (u <= 250)):
    cal_u = (50 * 2) + (100 * 3) + ((u - 150) * 5)
else:
    cal_u = (50 * 2) + (100 * 3) + (100 * 5) + ((u - 250) * 8)

   
surcharge = cal_u * 0.2 
bill = surcharge + cal_u
print(bill)
