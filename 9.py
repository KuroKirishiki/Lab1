import csv
import os
from PIL import Image

def z1():
    i = "C:/Users/nskde/PycharmProjects/9/8/2"

    if not os.path.exists("C:/Users/nskde/PycharmProjects/9/8/3"):
        os.mkdir("C:/Users/nskde/PycharmProjects/9/8/3")

    for f in os.listdir(i):
        if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png'):
            im = Image.open(os.path.join(i,f))
            im = im.resize((500, 500))
            im.save(os.path.join("C:/Users/nskde/PycharmProjects/9/8/3", f))
def z2():
    with open("data.csv") as f:
        t_readed = csv.reader(f, delimiter = ",")

        c = 0
        print("Надо купить")

        for row in t_readed:
            print(f'{row[0]} - {row[1]} шт. за {row[2]} руб.')
            c += 1
        print(f'Всего в файле {c} строк.')


z2()