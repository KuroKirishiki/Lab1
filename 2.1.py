
N = int(input("Введите количество слов: "))
chars = []

for i in range(N):
    chars.append(input())

    word = ' '.join(chars)

    print(word)

