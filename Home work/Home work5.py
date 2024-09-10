country_flags = {
    'kg': {'red', 'yellow'},  # Кыргызстан
    'ru': {'white', 'blue', 'red'},  # Россия
    'us': {'red', 'white', 'blue'},  # США
    'fr': {'blue', 'white', 'red'},  # Франция
    'ge': {'black', 'red', 'yellow'},  # Германия
    'it': {'green', 'white', 'red'},  # Италия
}


def find_countries_by_color(colors):
    matching_countries = set()
    for domain, flag_colors in country_flags.items():
        if colors.issubset(flag_colors):  # Проверяем все ли цвета присутствуют
            matching_countries.add(domain)
    return matching_countries


def main():
    while True:
        user_input = input("Введите цвет(а) (или 'выход' для завершения): ").strip().lower()

        if user_input == 'выход':
            print("Выход из программы.")
            break

        colors = set(user_input.split())

        # Проверяем, есть ли введенные цвета в словаре
        if any(color not in {color for colors in country_flags.values() for color in colors} for color in colors):
            print("Некоторые цвета не найдены в заданных флагах. Попробуйте снова.")
            continue

        if len(colors) == 1:
            # Если введен только один цвет
            matching_countries = {domain for domain, flag_colors in country_flags.items() if
                                  colors.issubset(flag_colors)}
            if matching_countries:
                print(f"Страны с цветом '{list(colors)[0]}': {', '.join(matching_countries)}")
            else:
                print(f"Нет стран с цветом '{list(colors)[0]}'.")
        else:
            # Если введено несколько цветов
            matching_countries = find_countries_by_color(colors)
            if matching_countries:
                print(f"Страны с цветами {', '.join(colors)}: {', '.join(matching_countries)}")
            else:
                print(f"Нет стран с цветами {', '.join(colors)}.")


if __name__ == "__main__":
    main()