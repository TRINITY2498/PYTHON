a = int(input())

five_hunderd = a // 500
fifty_note = (a % 500) // 50
ten_note = ((a % 500)%50) // 10 
one_note = (((a % 500)%50)%10) // 1 

print("500: "+str(five_hunderd), "50: "+str(fifty_note), "10: "+str(ten_note), "1: "+str(one_note))