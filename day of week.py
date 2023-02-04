day = int(input("Введите день: "))
match day % 7:
    case 1: day_of_week = "Понедельник"
    case 2: day_of_week = "Вторник"
    case 3: day_of_week = "Среда"
    case 4: day_of_week = "Четверг"
    case 5: day_of_week = "Пятница"
    case 6: day_of_week = "Суббота"
    case 0: day_of_week = "Воскресенье"

if 1 <= day <= 31:
    month = "января"
    day_of_month = day
elif 32 <= day <= 59:
    month = "февраля"
    day_of_month = day - 31
elif 60 <= day <= 90:
    month = "марта"
    day_of_month = day - 59
elif 91 <= day <= 120:
    month = "апреля"
    day_of_month = day - 90
elif 121 <= day <= 151:
    month = "мая"
    day_of_month = day - 120
elif 152 <= day <= 181:
    month = "июня"
    day_of_month = day - 151
elif 182 <= day <= 212:
    month = "июля"
    day_of_month = day - 181
elif 213 <= day <= 243:
    month = "августа"
    day_of_month = day - 212
elif 244 <= day <= 273:
    month = "сентября"
    day_of_month = day - 243
elif 274 <= day <= 304:
    month = "октября"
    day_of_month = day - 273
elif 305 <= day <= 334:
    month = "ноября"
    day_of_month = day - 304
elif 335 <= day <= 365:
    month = "декабря"
    day_of_month = day - 334
else:
    print("Выход за пределы")
    exit()
print(str(day_of_month) + " " + month + " - " + day_of_week)
