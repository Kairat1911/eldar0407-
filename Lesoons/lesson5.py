# Словари - dict, множества.

student = {
    'name': 'azamat',
    'age': 19,
    "weight": 65.3,
}

"""add"""
student['surname'] = 'musagaliev'
student.update({})
"""edit"""
"""delete"""

# print(students)
# print(students['name'])
# print(students['age'])

# print(type(students))














#
# numbers_1 = [1, 2, 3, 2, 1, 4, 3, 5, 1 ]
# numbers_2 = {1, 2, 3, 2, 1, 4, 3, 5, 1 }
#
# print(numbers_1)
# print(numbers_2)

behbarmak = {'мясо', "тесто", "лук"}
plov = {'мясо' "рис", "морковь"}


print(behbarmak.union(plov))
print(behbarmak.intersection(plov))
print(behbarmak.difference(plov))
print(behbarmak.symmetric_difference(plov))