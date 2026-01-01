s = input()

s = s.lower()

reverse = ""

for ch in s:
    reverse = ch + reverse
    
is_palindrome = (s == reverse)

if is_palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")