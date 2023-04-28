import random

def z1():
    list = []
    for i in range(5):
        list.append(random.randint(0, 10))
    a = int(input("Введите число: "))
    if a in list:
        print("Yes", *list)
    else:
        print("No", *list)

from random import randint

def z2():
    list = []
    for i in range(5):
        j = randint(0, 10)
        list.append(j)
    print(*list)
    print(*filter(lambda x : list.count(x)> 1, list))

def z3():
    n = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    d = int(input("Сколько выходных? "))
    print("Работа:", *n[:-d])
    print("Выходные:", *n[-d:])

def z4():
    l = ['Пушкин', 'Толстой', 'Кузнецов', 'Горшенёв', 'Францев', 'Солодилов', 'Носов', 'Лобов', 'Моргун', 'Шейкина']
    l2 = ['Снейк', 'Бриджес', 'Лютор', 'Лэйн', 'Уэйн', 'Пушкин', 'Аллен', 'Малфой', 'Роберт', 'Пирс']
    n = tuple(random.sample(l,5) + random.sample(l2, 5))
    print(*l)
    print(*l2)
    print(*n)
    print(len(n))
    if 'Пушкин' in n:
        print(n.count('Пушкин'))
    else:
        print("no")


z4()