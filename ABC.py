a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a % 2 == 0:
    if b % 2 != 0:
        print("а) +")
    else:
        print("а) -")
elif b % 2 == 0:
    if a % 2 != 0:
        print("а) +")
    else:
        print("а) -")
else:
    print("а) -")

if a % 3 == 0 and b % 3 == 0 and c % 3 == 0:
    print("б) +")
else:
    print("б) -")