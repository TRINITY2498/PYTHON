n = int(input())

if n < 3:
    print("Not Polygon")
elif n == 3:
    print("Triangle")
elif n == 4:
    print("Quadrilateral")
elif n == 5:
    print("Pentagon")
else:
    print("Big Polygon")