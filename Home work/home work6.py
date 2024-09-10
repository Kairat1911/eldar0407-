# Словарь для хранения информации о фильмах и их рейтингах
movies = {
    "Django Unchained": {
        "John": 10,
        "Jack": 9
    }
}


def add_movie():
    title = input("Введите название фильма: ").strip().title()
    if title in movies:
        print("This movie already exists!")
    else:
        movies[title] = {}
        print("Movie added successfully.")


def add_rating():
    title = input("Введите название фильма для добавления рейтинга: ").strip().title()
    if title not in movies:
        print("This movie doesn't exist.")
        return

    username = input("Введите ваше имя пользователя: ").strip()
    rating = input("Введите вашу оценку (от 0 до 10): ").strip()

    try:
        rating = int(rating)
        if rating < 0 or rating > 10:
            print("Оценка должна быть от 0 до 10.")
            return
    except ValueError:
        print("Пожалуйста, введите числовую оценку.")
        return

    movies[title][username] = rating
    print(f"Rating added successfully for {title}.")


def main():
    while True:
        print("\n1. Добавить фильм")
        print("2. Добавить рейтинг к фильму")
        print("3. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == '1':
            add_movie()
        elif choice == '2':
            add_rating()
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()