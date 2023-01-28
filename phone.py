t = 11 * 60
dt = 15
s = 10
d = 6

t2 = t + dt

if t2 >= 24:
    d += (t + dt / 60) // 24
    while d > 7:
        d = d - 7

# Классические случаи
if d >= 6:
    if t < 8 or t >= 22:
        plata = s * dt * 0.7
    else:
        plata = s * dt * 0.9
else:
    if t < 8 or t >= 22:
        plata = s * dt * 0.8

for t in range(t2):
    if t < 8*60 or t >= 22*60:
        plata += s * 0.8
    plata += s
    t = t + 1

print(plata)

