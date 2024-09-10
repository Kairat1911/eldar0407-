# def get_daily_expenses():
#     expenses = []
#     days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
#
#     for day in days_of_week:
#         while True:
#             try:
#                 expense = float(input(f'Укажите расход на {day}: '))
#                 expenses.append(expense)
#                 break
#             except ValueError:
#                 print("Пожалуйста, введите корректное число.")
#
#     return expenses
#
# def calculate_expenses(expenses):
#     total_expense = sum(expenses)
#     average_expense = round(total_expense / len(expenses), 1)
#     return total_expense, average_expense
#
# def main():
#     expenses = get_daily_expenses()
#     total, average = calculate_expenses(expenses)
#
#     print(f'Сумма расходов на неделю: {total}')
#     print(f'Средний расход на день: {average}')
# if __name__ == '__main__':
#     main()
#
#
#
# def main():
#     while True:
#         color = input("Введите цвет светофора (зеленый, желтый, красный) или 'выход' для завершения: ").strip().lower()
#
#         if color == "выход":
#             print("Выход из программы.")
#             break
#         elif color == "красный":
#             print("Стой!")
#         elif color == "желтый":
#             print("Приготовься!")
#         elif color == "зеленый":
#             print("Иди!")
#         else:
#             print("Неверный запрос. Пожалуйста, введите 'красный', 'желтый', 'зеленый' или 'выход'.")
#
#
# if __name__ == "__main__":
#     main()

# geektech = {
#     'name': 'Geektech',
#     'address': 'Токтогула 175',
#     'courses': {'Backend', 'Android'}
# }
#
#
#
#
# geeks = dict(name='GEEKS', address='Ибраимова 103')
# geektech.update(geeks)
# geeks = geektech.copy()
# geeks ['courses' ].update(['Frontend', 'i0S'])
# print (geeks)

# for i in range(1, 10+1):
#     if i > 7:
#         print(i)
#     else:
#         print(False)


# counter = 5
#
# while counter != 0:
#     print ( 'GEEKS. Python, first month, final test!')
#     counter -= 1

# geeks_in = ['Бишкек', 'Ош', 'Кара-Балта', 'Бишкек 9мкр ' ]
#
# geeks_in.sort()
# geeks_in = [i.upper() for i in geeks_in]
#
# geeks_in = geeks_in[ : :- 1]
# print(geeks_in)


# kgz_regions = [
#     "Чуй", "Ыссык-Кел", "Нарын", "Талас",
#     "Джалал-Абад", "Ош","Баткен"
#     ]
#
#
# first_three = tuple(kgz_regions [:3])
# print (first_three)
#
# geeks_founding_year = 2018
# current_year = int(input('Введите текущий год: '))
#
# if (current_year - geeks_founding_year) > 5:
#     print('Образовательному центру больше 5 лет')
# elif (current_year - geeks_founding_year) in range(1, 6):
#     print('Образовательному центру меньше 5 лет')
# else:
#     pass