string = input()

string = string.lower()

if string == string[len(string) - 1: : -1]:
    print("True")
else:
    print("False")