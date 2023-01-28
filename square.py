while True:
    x = float(input("x="))
    y = float(input("y="))
    if abs(x) <= 1 and abs(y) <=1:
        if abs(y) >= 1-abs(x):
            print("Попало")
    else: print ("Выход из диапазона")
    print(x, y)
    if input("Выход как в vim, для продолжения нажмите enter ") == ":wq!": exit()
