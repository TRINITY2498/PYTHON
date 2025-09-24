w = input()

w_len = len(w) - 4

ans = (w[ : 2]) + ("*"*w_len) + (w[len(w) -2 : ])

print(ans)