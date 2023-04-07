def zd3():
    from random import randint
    import sys
    kp = 0
    knp = 0
    while knp != 3:
        while True:
            x = randint(1,50)
            y = randint(1,50)
            print(f" {x} + {y} = ", end="")
            r = input()
            if r == "stop":
                print('игра закончена, верных ответов: ', kp)
                sys.exit()
            r = int(r)
            if x+y==r:
                kp+=1
            else:
                print('ошибка')
                knp+=1
            if knp == 3:
                print('игра закончена, верных ответов: ', kp)
                break
zd3()
