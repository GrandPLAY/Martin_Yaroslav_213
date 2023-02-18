from random import *
numbers = list()
while 0 not in numbers:
    numbers.append(randint(-10, 10))
length = len(numbers)
change = 0
for i in range(length):
    if numbers[i] > 0 and numbers[i+1] < 0 or numbers[i] < 0 and numbers[i+1] > 0:
        change += 1
print(numbers)
print(change)
