from random import *

numbers = list()
minus = list()
plus = list()

while -1000 not in numbers:
    numbers.append(randint(-1000, 1000))

lengthnum = len(numbers)

for i in range(lengthnum):
    if numbers[i] < 0:
        minus.append(numbers[i])
    elif numbers[i] > 0:
        plus.append(numbers[i])

lengthmin = len(minus)
lengthpls = len(plus)
summin = 0
sumpls = 0

for i in range(lengthmin):
    summin += minus[i]
arithmeanmin = summin / lengthmin
for i in range(lengthpls):
    sumpls += plus[i]
arithmeanpls = sumpls / lengthpls

print("Все: " + str(numbers))
print("Отрицательные: " + str(minus))
print("Положительные: " + str(plus))
print("Ср. арифм. отрицательных: " + str(arithmeanmin))
print("Ср. арифм. положительных: " + str(arithmeanpls))