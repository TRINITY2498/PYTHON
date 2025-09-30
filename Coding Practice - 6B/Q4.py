a = int(input())

hundred_note = a // 100
rem1 = a % 100

fifty_note = rem1 // 50 
rem2 = rem1 % 50 

ten_note = rem2 // 10
rem3 = rem2 % 10

one_note = rem3 // 1

print("100:"+str(hundred_note))
print("50:"+str(fifty_note))
print("10:"+str(ten_note))
print("1:"+str(one_note))
