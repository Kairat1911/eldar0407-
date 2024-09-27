def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # обмен элементов
    return arr

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        # Проверяем, является ли элемент средним
        if arr[mid] == target:
            return mid  # возвращаем индекс найденного элемента
        # Если элемент больше, то он может быть только в правой половине
        elif arr[mid] < target:
            left = mid + 1
        # Если элемент меньше, то он может быть только в левой половине
        else:
            right = mid - 1
    return -1  # элемент не найден

# Неотсортированный список
unsorted_list = [64, 34, 25, 12, 22, 11, 90]

# Сортируем список
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)

# Элемент для поиска
target = 22

# Выполняем двоичный поиск
result = binary_search(sorted_list, target)

# Выводим результат поиска
if result != -1:
    print(f"Элемент {target} найден на индексе {result}.")
else:
    print(f"Элемент {target} не найден.")
