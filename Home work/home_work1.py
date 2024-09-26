# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
while True:
Monday = int(input('Укажите расход на понедельник:'))
Tuesday = int(input('Укажите расход на вторник:'))
Wednesday = int(input('Укажите расход на среду:'))
Thursday = int(input('Укажите расход на четверг:'))
Friday = int(input('Укажите расход на пятницу:'))
Saturday = int(input('Укажите расход на субботу:'))
Sunday = int(input('Укажите расход на воскресенье:'))
summa = Monday + Tuesday + Wednesday + Thursday + Friday + Saturday + Sunday
days = 7
print(f'сумма расходов на неделю: {summa}')
average_consumption = summa / days
average_consumption = round(average_consumption, 1)
print(f'средний расход на день: {average_consumption}')
if 1 <= summa <= 500:
    print('мало')
elif  501 <= summa <= 700:
    print('средне')
elif  701 < summa :
    print('много')
else:
    print('ничего не потрачено')
