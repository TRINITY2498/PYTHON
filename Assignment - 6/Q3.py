d = int(input())

hundred_note = d // 100
fifty_note = (d % 100) // 50
twenty_note = ((d % 100)%50) // 20
ten_note = (((d % 100)%50)%20) // 10 

print("100 Notes: "+str(hundred_note))
print("50 Notes: "+str(fifty_note))
print("20 Notes: "+str(twenty_note))
print("10 Notes: "+str(ten_note))