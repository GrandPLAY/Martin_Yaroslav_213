from random import *
a = list()
for i in range(200):
    a.append(randint(-1000, 1000))
b = len(a)
c = 0
print(a)
while b >= 0:
    i = f = c
    for i in range(b-1):
        if a[i] > a[i+1]:
            first = a[i]
            second = a[i+1]
            a[i] = second
            a[i+1] = first
    for f in range(b-1):
        if a[b-f-2] > a[b-f-1]:
            first = a[b-f-2]
            second = a[b-f-1]
            a[b-f-2] = second
            a[b-f-1] = first
    b -= 1
    c += 1
print(a)
