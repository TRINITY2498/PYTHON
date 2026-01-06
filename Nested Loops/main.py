
for a in range(3):
    print("outer :" + str(a))
    
    for b in range(7,9):
        print(" inner :" + str(b))

print("End")
    

"""

n = int(input())

for row_num in range(1,n + 1):
    row_out = ""
    
    for seq_num in range(1,row_num + 1):
        row_out = row_out + str(seq_num) + " "
    
    print(row_out)

"""