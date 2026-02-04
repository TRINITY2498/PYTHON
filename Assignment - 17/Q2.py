T = input()

unit = T[-1]

digit = float(T[ : -1])

if unit == "C":
    
    c = (float(digit))
    
    f = (float(c * 1.8) + 32)
    
    k = (float(c + 273))
    
    print(str(round(c,2)) + "C")
    print(str(round(f,2)) + "F")
    print(str(round(k,2)) + "K")

elif unit == "F":
    
    f = (float(digit))
    
    c = (float((f - 32) / (1.8))) 
    
    k = float(c + 273)
    
    print(str(round(c,2)) + "C")
    print(str(round(f,2)) + "F")
    print(str(round(k,2)) + "K")


elif unit == "K":
    
    k = float(digit)
    
    c = float(k - 273)
    
    f = (float(c * 1.8) + 32)
    
    print(str(round(c,2)) + "C")
    print(str(round(f,2)) + "F")
    print(str(round(k,2)) + "K")