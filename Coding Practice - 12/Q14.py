row = int(input())
column = int(input())

result = ""

for i in range(1,column + 1):
    result = result + str(i) + " "
    
for j in range(row):
    print(result)
