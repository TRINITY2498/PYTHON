a = int(input())

two_thousand = a // 2000 
five_hundred = (a % 2000) // 500
two_hundred = ((a % 2000)%500) // 200 
fifty_note = (((a % 2000)% 500) % 200) // 50
twenty_note = ((((a % 2000)%500)%200)%50) // 20 
five_note = (((((a % 2000)%500)%200)%50)%20) // 5 
two_note = ((((((a % 2000)%500)%200)%50)%20)%5) // 2 
one_note = (((((((a % 2000)%500)%200)%50)%20)%5)%2) // 1 

print("2000:"+str(two_thousand), "500:"+str(five_hundred), "200:"+str(two_hundred), "50:"+str(fifty_note), "20:"+str(twenty_note), "5:"+str(five_note), "2:"+str(two_note), "1:"+str(one_note))