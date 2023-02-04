num = int(input("Введите кол-во копеек от 1 до 99: "))
if num < 1 or num > 99:
    print("Выход за пределы")
    exit()
if num // 10 == 1:
    name = " копеек"
else:
    match num % 10:
        case 1: name = " копейка"
        case 2 | 3 | 4: name = " копейки"
        case _: name = " копеек"
print(str(num) + name)
