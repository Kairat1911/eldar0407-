file = open('results.txt', 'w')

import random


def main():
    while True:
        print("Загадайте число от 1 до 100 и нажмите Enter.")
        input("Нажмите Enter, когда будете готовы...")

        low = 1
        high = 100
        attempts = 0
        guesses = []

        while True:
            attempts += 1
            guess = random.randint(low, high)
            guesses.append(guess)
            print(f"Я думаю, это {guess}.")

            response = input("Ваш ответ (да/больше/меньше)? ").strip().lower()

            if response == "да":
                print(f"Ура! Я угадал ваше число {guess} за {attempts} попыток.")
                with open('results.txt', 'a') as file:
                    file.write(f"Загаданное число: {guess}, Попытки: {attempts}, Список попыток: {guesses}\n")
                break
            elif response == "больше":
                low = guess + 1
            elif response == "меньше":
                high = guess - 1
            else:
                print("Пожалуйста, отвечайте 'да', 'больше' или 'меньше'.")


if __name__ == "__main__":
    main()