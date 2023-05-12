from PIL import Image, ImageDraw

def z1():
    i = Image.open('8m.jpg')
    i_c = i.crop((100, 75, 500, 550))
    i_c.save('uu.jpg')

def z2():
    f = { '8 марта': '8m.jpg',
          'Новый год': 'Ника_postcard.png',
          '23 февраля': '23f.jpg'
          }
    h = input("gjjhjj: ")
    if h in f:
        z = f[h]
        g = Image.open(z)
        g.show()

def z3():
    i = Image.open('23f.jpg')
    y = ImageDraw.Draw(i)
    y.text((100, 150), "Hello World!", fill='black')
    i.save('hi.jpg')

z2()