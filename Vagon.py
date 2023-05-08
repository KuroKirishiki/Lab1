a = int(input("Введите ваше место: "))
print()
if a % 2 == 0 and a <= 36:
    print("Ваше место в купе сверху")
elif a % 2 != 0 and a <=35:
    print("Ваше место в купе снизу")
elif a % 2 == 0 and a > 36 and a <= 54:
    print("Ваше место сбоку сверху")
elif a % 2 != 0 and a > 35 and a <= 54:
    print("Ваше место сбоку снизу")
else:
    print("вы неправильно ввели место")
