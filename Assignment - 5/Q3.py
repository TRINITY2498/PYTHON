m = int(input())

winter = ((m == 1) or (m == 12) or (m == 11))
spring = ((m == 2) or (m == 3))
summer = ((m == 4) or (m == 5) or (m == 6))
rainy = ((m == 7) or (m == 8))
autumn = ((m == 9) or (m == 10))

if winter:
    print("Winter")
elif spring:
    print("Spring")
elif summer:
    print("Summer")
elif rainy:
    print("Rainy")
elif autumn:
    print("Autumn")