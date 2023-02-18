from random import *

numbers = list()
checknum = list()
check = True

for i in range(int(input("Сколько чисел сгенерировать: "))):
    numbers.append(randint(-1000, 1000))
print(numbers)

length = len(numbers)

numbers.sort()
for i in range(length - 1):
    if numbers[i] == numbers[i+1]:
        check = False
        checknum.append(numbers[i])

if check:
    print("Все числа уникальны")
else:
    print("Есть повторения: " + str(checknum))
