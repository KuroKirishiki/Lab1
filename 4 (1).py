def z1():
    try:
        x = int(input("Введите число: "))
        y = x % 3
    except ValueError:
        print("Введено не число")
    else:
        if y == 0:
            print("Число кратно трём")
        else:
            print("Число не кратно трём")

def z2():
    try:
        x = int(input("Введите число: "))
        y = x / 100
    except ValueError:
        print("Введено не число")
    except ZeroDivisionError:
        print("Введён ноль")
    else:
        print(y)
def z3():
        x = input("Введите дату:")
        x = x.split('.')
        y = int(x[0]) * int(x[1])
        if y == int(x[2]):
            print("Дата магическая")
        else:
            print("Дата обычная")
def z4():
    x = input("Введите ваш номер билета: ")
    if len(x) % 2 == 0:
        for i in x[0:int((int(len(x))/2))]:
            s1 = s1 + int(i)
        for i in x[int((int(len(x))/2)):int(int(len(x)) + 1)]:
            s2 = s2 + int(i)
        if s1 == s2 :
            print('билет счастливый')
        else:
            print('билет не счастливый')
    else:
        print("Неверное кол-во символов")

zd4()
