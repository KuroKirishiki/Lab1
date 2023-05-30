def z1():
    class Restor:

        def __init__(self, restor_name, cuisine_type):
            self.restor_name = restor_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название ресторана {self.restor_name}, кухня: {self.cuisine_type}')

        def open_restaurant(self):
            print('открыто')


    o = Restor('Карие очи', 'Кавказская')
    print(o.restor_name)
    print(o.cuisine_type)

    o.open_restaurant()
    o.describe_restaurant()

def z2():
    class Restor:

        def __init__(self, restor_name, cuisine_type):
            self.restor_name = restor_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название ресторана {self.restor_name}, кухня: {self.cuisine_type}')

        def open_restaurant(self):
            print('открыто')

    u = input("ресторан: ")
    u1 = input("кухня: ")
    o = Restor(u, u1)
    print(o.restor_name)
    print(o.cuisine_type)
    o.open_restaurant()
    o.describe_restaurant()

    t = input("ресторан: ")
    t1 = input("кухня: ")
    o = Restor(t, t1)
    print(o.restor_name)
    print(o.cuisine_type)
    o.open_restaurant()
    o.describe_restaurant()

    y = input("ресторан: ")
    y1 = input("кухня: ")
    o = Restor(y, y1)
    print(o.restor_name)
    print(o.cuisine_type)
    o.open_restaurant()
    o.describe_restaurant()

def z3():
    class Restor:

        def __init__(self, restor_name, cuisine_type, ret):
            self.restor_name = restor_name
            self.cuisine_type = cuisine_type
            self.ret = ret

        def describe_restaurant(self):
            print(f'Название ресторана {self.restor_name}, кухня: {self.cuisine_type}')

        def open_restaurant(self):
            print('открыто')

    o = Restor('Карие очи', 'Кавказская', 5)
    print(o.restor_name)
    print(o.cuisine_type)
    print(f'Старый рейтинг {o.ret}')
    f = input("Введите новый рейтинг: ")
    o.ret = f
    print(o.ret)
    o.open_restaurant()
    o.describe_restaurant()

z3()