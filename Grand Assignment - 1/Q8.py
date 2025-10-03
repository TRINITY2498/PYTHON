n = int(input())

thousand_note = n // 1000
five_hundred = (n % 1000) // 500
hundred_note = ((n % 1000)% 500) // 100 
fifty_note = (((n % 1000)% 500)% 100) // 50 
twenty_note = ((((n % 1000)% 500)% 100)% 50) // 20 
five_note = (((((n % 1000)% 500)%100)%50)% 20) // 5 
one_note = ((((((n % 1000)% 500)% 100)% 50)% 20)% 5) // 1 

print("1000:"+str(thousand_note))
print("500:"+str(five_hundred))
print("100:"+str(hundred_note))
print("50:"+str(fifty_note))
print("20:"+str(twenty_note))
print("5:"+str(five_note))
print("1:"+str(one_note))