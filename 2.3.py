word=input('Введите слово: ')
for i in word:
    if (i=="ф") | (i=="Ф"):
        print('Ого! Вы ввели редкое слово!')
    break
else:
     print("Эх, это не редкое слово!")