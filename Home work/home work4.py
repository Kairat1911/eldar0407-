mentors = ["Тимур", "Арсен", "Гулина", "Даниель"]

while True:
    print("\nВыберите команду:")
    print("1) Добавление")
    print("2) Изменение")
    print("3) Удаление")
    print("0) Выход")

    command = input("Введите номер команды: ")

    if command == "1":  # Добавление
        if len(mentors) >= 10:
            print("Список менторов уже полон.")
            continue

        new_mentor = input("Введите имя ментора (не более 15 букв): ").strip()
        if len(new_mentor) > 15:
            print("Имя не должно превышать 15 букв.")
            continue

        new_mentor = new_mentor.title()

        if new_mentor in mentors:
            print("Такое имя уже есть в списке.")
            mentors_tuple = tuple(mentors)
            print("Список менторов:", mentors_tuple)
        else:
            mentors.append(new_mentor)
            print(f"{new_mentor} добавлен в список менторов.")

    elif command == "2":  # Изменение
        old_name = input("Введите имя заменяемого ментора: ").strip().title()

        if old_name not in mentors:
            print("Введенное имя не найдено в списке.")
            continue

        new_name = input("Введите новое имя ментора (не более 15 букв): ").strip()
        if len(new_name) > 15:
            print("Имя не должно превышать 15 букв.")
            continue

        new_name = new_name.title()

        if new_name in mentors:
            print("Такое имя уже есть в списке.")
        else:
            index = mentors.index(old_name)
            mentors[index] = new_name
            print(f"{old_name} изменен на {new_name}.")
            mentors_tuple = tuple(mentors)
            print("Список менторов:", mentors_tuple)

    elif command == "3":  # Удаление
        print("Выберите способ удаления:")
        print("1) По индексу")
        print("2) По имени")

        delete_method = input("Введите номер метода: ")

        if delete_method == "1":
            index = int(input(f"Введите индекс (0-{len(mentors) - 1}): "))
            if 0 <= index < len(mentors):
                removed_mentor = mentors.pop(index)
                print(f"{removed_mentor} удален из списка.")
                mentors_tuple = tuple(mentors)
                print("Список менторов:", mentors_tuple)
            else:
                print("Некорректный индекс.")

        elif delete_method == "2":
            name_to_remove = input("Введите имя ментора для удаления: ").strip().title()
            if name_to_remove in mentors:
                mentors.remove(name_to_remove)
                print(f"{name_to_remove} удален из списка.")
                mentors_tuple = tuple(mentors)
                print("Список менторов:", mentors_tuple)
            else:
                print("Введенное имя не найдено в списке.")

    elif command == "0":  # Выход
        mentors_tuple = tuple(mentors)
        print("Список менторов:", mentors_tuple)
        break

    else:
        print("Некорректная команда. Пожалуйста, попробуйте снова.")