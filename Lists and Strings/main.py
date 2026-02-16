# split

"""

nums = "1 2 3 4"

nums_list = nums.split()
print(nums_list)

"""
"""

nums = "1\n2\t3 4"

num_list = nums.split()

print(num_list)

"""
"""

nums = "1,2,3,4"

num_list = nums.split(',')

print(num_list)

"""
"""

nums = "1,2,,3,4"

num_list = nums.split(',')

print(num_list)

"""
"""

nums = "1   2 3 4"

num_list = nums.split(' ')

print(num_list)

"""
"""

string_a = "Python is a Programming Language"
list_a = string_a.split('a')
print(list_a)

"""

"""

string_a = "step-by-step execution of code"
list_a = string_a.split('step')
print(list_a)

"""

# Joins

"""

list_a = ['Python is ', ' Progr', 'mming l', 'ngu', 'ge']
string_a = "a".join(list_a)
print(string_a)

"""

"""

list_a = [5,4,3,2,1]

item = list_a[-1]

print(item)

"""

"""

list_a = [5,4,3,2,1]

item = list_a[-3:-1]

print(item)

"""