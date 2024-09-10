class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        marital_status = "женат" if self.is_married else "не женат"
        print(f"Меня зовут {self.fullname}, мне {self.age} лет, я {marital_status}.")


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average_mark(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)


class Teacher(Person):
    base_salary = 50000  # Пример базовой зарплаты

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        bonus = 0.05 * max(0, self.experience - 3) * Teacher.base_salary
        return Teacher.base_salary + bonus


def create_students():
    students = [
        Student("Иван Иванов", 16, False, {"математика": 5, "физика": 4}),
        Student("Мария Петрова", 17, False, {"математика": 3, "история": 5}),
        Student("Сергей Сидоров", 15, False, {"физика": 4, "химия": 5}),
    ]
    return students


# Пример использования классов и функций
teacher = Teacher("Александр Смирнов", 40, True, 5)
teacher.introduce_myself()
print(f"Зарплата учителя: {teacher.calculate_salary()}")

students = create_students()
for student in students:
    student.introduce_myself()
    print("Оценки:", student.marks)
    print("Средняя оценка:", student.average_mark())