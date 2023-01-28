plata = 0
t = int(input("Начало разговора - часов: ")) * 60 + int(input("Начало разговора - минут: "))
dt = int(input("Время разговора (мин): "))
s = int(input("Тариф (руб/мин): "))
d = int(input("День недели (порядковым числом): "))

t2 = t + dt
while t != t2:
    if d >= 6:
        if t < 8*60 or t >= 22*60:
            plata += s * 0.72
        else:
            plata += s * 0.9
    else:
        if t < 8*60 or t >= 22*60:
            plata += s * 0.8
        else:
            plata += s
    t = t + 1
    if t >= 24 * 60:
    	if d == 7:
    		d = 1
    	else:
    		d += 1
    	t -= 24 * 60
    	t2 -= 24 * 60
print("Итоговая сумма: " + str(plata))
