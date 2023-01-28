plata = 0
t = 7 * 60 + 45
dt = 237
s = 100
d = 6

t2 = t + dt

for t in range(t2):
    print (d)
    if d >= 6:
        if t < 8*60 or t >= 22*60:
            plata += s * 0.7
        else:
            plata += s * 0.9
    else:
        if t < 8*60 or t >= 22*60:
            plata += s * 0.8
        else:
            plata += s
    t = t + 1
    if t > 24 * 60:
        d += 1
        t -= 24 * 60
        t2 -= 24 * 60
print(plata)
