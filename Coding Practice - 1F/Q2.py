w = input()
n = int(input())

w_len = len(w) - 3 
last_three = w[w_len : ]
print(last_three * n)