s = input()
n = int(input())

words = s.split()

print(words[ : -(n + 1) : -1])