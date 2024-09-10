def nearest_number(numbers, target):
    # Сортируем список по расстоянию до целевого числа
    sorted_numbers = sorted(numbers, key=lambda x: abs(x - target))
    return (target, sorted_numbers)

# Пример использования
result = nearest_number([10, 20, 30, 40], 25)
print(result)  # (25, [20, 30, 10, 40])

# Фильтруем четные числа из списка
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6]


# Увеличиваем каждое число в списке на 1
numbers = [1, 2, 3, 4, 5]
incremented_numbers = list(map(lambda x: x + 1, numbers))
print(incremented_numbers)  # [2, 3, 4, 5, 6]


def get_element_by_index(iterable):
    while True:
        index = input(f"Введите индекс (от 0 до {len(iterable) - 1}) или 'выход' для завершения: ")
        if index.lower() == 'выход':
            break
        try:
            index = int(index)
            print(f"Элемент по индексу {index}: {iterable[index]}")
        except IndexError:
            print(f"Неверный индекс. Пожалуйста, введите индекс от 0 до {len(iterable) - 1}.")
        except ValueError:
            print("Пожалуйста, введите корректное число или 'выход'.")

# Пример использования
get_element_by_index([10, 20, 30, 40, 50])
