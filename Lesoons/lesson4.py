# списки-List Индексы и срезы, Встроенные функции к наборам элементов.
# список включение List comprehension. [object, cycle, condition]
# Кортежи - typle

numbers =('word', True, 34,56.1)
print(type(numbers))


# print(len(numbers))
# сколько переменых в списке.
# print(sum(numbers))
# суммма пременых.
# print(min(numbers))
# минимальное значение.
# print(max(numbers))
# максимальное заначение.

students = ['nurlym', 'esentur','kairat', 'emir','coholpon','danyar']
students_2 = [name.title() for name in students]
students_2 = [name.title() for name in students if 'a' not in name]
print(students)
print(students_2)

# students_copy = students
# students_copy = students.copy()
# students[0] = 'tom'
# print(id(students))
# print(id(students_copy))
# print(students == students_copy)
# print(students is students_copy)
# print(students)
# print(students_copy)

# """add"""
# students.append('adina')
# students.insert(1,'kudratilla')
# students.extend(['danil', 'saadat'])

 # """edit"""
# students[3] = 'akel'
# students[0] = 'karim'
# students.sort()
# students.sort(reverse=True)
# students.reverse

 # """delete"""
# students.remove('kairat')
# students.pop(0)
# print(students)
# del students[1:3]

# """"индексы"""
# print(students[0])
# print(students[3])
# print(students[-1])

# """срезы"""
# # схемы срезов - [start:stop:step]
# print(students[1:3])
# print(students[-2:])
# print(students[:2])
# print('123456789'[::2])
# print('123456789'[:-1])
# print(type(students))






