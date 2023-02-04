era = input("Введите эру (До нашей эры - 0, нашей эры - 1): ")
match era:
    case "0": era = " до нашей эры"
    case "1": era = " нашей эры"
    case _:
        print("Неверный ввод")
        exit()
year = int(input("Введите год (максимум 2000): "))
if year > 2000:
    print("Нам запретили считать больше 2000:(")
    exit()
if year % 4 == 0:
    print(str(year) + " год" + era + " - високосный")
else:
    print(str(year) + " год" + era + " - не високосный")