day = int(input("введите день рождения:"))
mount = int(input('введите месяц рождения:'))
if day >= 21 and day <= 31 and mount == 3 or day >= 1 and day <= 20 and mount == 4:
    print('Овен')
elif day >= 21 and day <= 30 and mount == 4 or day >= 1 and day <= 21 and mount == 5:
    print('Телец')
elif day >= 22 and day <= 31 and mount == 5 or day >= 1 and day <= 21 and mount == 6:
    print('Близнецы')
elif day >= 22 and day <= 30 and mount == 6 or day >= 1 and day <= 22 and mount == 7:
    print('Рак')
elif day >= 23 and day <= 31 and mount == 7 or day >= 1 and day <= 21 and mount == 8:
    print('Лев')
elif day >= 22 and day <= 31 and mount == 8 or day >= 1 and day <= 23 and mount == 9:
    print('Дева')
elif day >= 24 and day <= 30 and mount == 9 or day >= 1 and day <= 23 and mount == 10:
    print('Весы')
elif day >= 24 and day <= 31 and mount == 10 or day >= 1 and day <= 22 and mount == 11:
    print('Скорпион')
elif day >= 23 and day <= 30 and mount == 11 or day >= 1 and day <= 22 and mount == 12:
    print('Стрелец')
elif day >= 23 and day <= 31 and mount == 12 or day >= 1 and day <= 20 and mount == 1:
    print('Козерог')
elif day >= 21 and day <= 31 and mount == 1 or day >= 1 and day <= 19 and mount == 2:
    print('Водолей')
elif day >= 20 and day <= 29 and mount == 2 or day >= 1 and day <= 20 and mount == 3:
    print('Рыбы')
else:
    print('неправильно введена дата рождение')