from random import *
a = list()
for i in range(5000):
    a.append(randint(-1000, 1000))
b = len(a)
print(a)
while b > 0:
    for i in range(b-1):
        if a[i] > a[i+1]:
            first = a[i]
            second = a[i+1]
            a[i] = second
            a[i+1] = first
    b -= 1
print(a)
