s = input()

reversed_s = ""

for ch in s:
    reversed_s = ch + reversed_s
is_palindrome = (s == reversed_s)

print(is_palindrome)