s = input()

s = s.lower()
s = s.replace(" ","")
s = s.replace("'","")
reverse = ""

for ch in s:
    reverse = ch + reverse 
    
is_palindrome = (s == reverse)

if is_palindrome:
    print("True")
else:
    print("False")
    