'''
# unpacking

tuple_a = tuple("Red")
print(tuple_a)

(s_1, s_2, s_3) = tuple_a 

print(s_1)
print(s_2)
print(s_3)

'''

'''
# Packing

a = 1,2,3
 
print(type(a))

print(a)

'''

'''
a,b,c = 1,2, "Hi"

print(a)
print(b)
print(c)

'''

'''
def get_sum_and_product(a, b):
    
    num_sum = a + b 
    num_product = a * b
    
    return num_sum, num_product 
    
x,y = get_sum_and_product(2, 3)

print(x)
print(y)

'''