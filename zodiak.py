day = int(input("День: "))
month = int(input("Месяц: "))

if day >= 24:
    match month:
        case 8: zodiak = "Дева"
        case 9: zodiak = "Весы"
        case 10: zodiak = "Скорпион"
elif day >= 23:
    match month:
        case 7: zodiak = "Лев"
        case 11: zodiak = "Стрелец"
elif day >= 22:
    match month:
        case 6: zodiak = "Рак"
        case 12: zodiak = "Козерог"
elif day >= 21:
    match month:
        case 1: zodiak = "Водолей"
        case 3: zodiak = "Овен"
        case 4: zodiak = "Телец"
        case 5: zodiak = "Близнецы"
elif day >= 19:
    if month == 2: zodiak = "Рыбы"
else:
    match month:
        case 1: zodiak = "Козерог"
        case 2: zodiak = "Водолей"
        case 3: zodiak = "Рыбы"
        case 4: zodiak = "Овен"
        case 5: zodiak = "Телец"
        case 6: zodiak = "Близнецы"
        case 7: zodiak = "Рак"
        case 8: zodiak = "Лев"
        case 9: zodiak = "Дева"
        case 10: zodiak = "Весы"
        case 11: zodiak = "Скорпион"
        case 12: zodiak = "Стрелец"
print(zodiak)
