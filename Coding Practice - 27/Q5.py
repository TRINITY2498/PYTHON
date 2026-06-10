n = int(input())



multi_of_2 = set()

multi_of_3 = set()



list_1 = []

list_2 = []

 

for i in range(1,n + 1):

    

    multi_of_2.add(i * 2)



for j in range(1,n + 1):

    

    multi_of_3.add(j * 3)

    



difference = multi_of_2 - multi_of_3



for p in difference:

    

    list_1 += [p]



list_1.sort()



symm_diff = multi_of_2 ^ multi_of_3 



for q in symm_diff:

    

    list_2 += [q]



list_2.sort()



print(list_1)

print(list_2)

