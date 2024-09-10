def is_vowel(letter):
    vowels = "aeiouyAEIOUYаеиоуюяёыЭАЕИОУЫЯЁ"
    return letter in vowels


def is_consonant(letter):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZбвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    return letter in consonants


while True:
    word = input("Введите слово на латинице или кириллице (или 'выход' для завершения): ")

    if word.lower() == 'выход':
        break

    total_letters = len(word)
    vowel_count = sum(1 for letter in word if is_vowel(letter))
    consonant_count = sum(1 for letter in word if is_consonant(letter))

    print(f"Общее количество букв: {total_letters}")
    print(f"Количество гласных букв: {vowel_count}")
    print(f"Количество согласных букв: {consonant_count}")

    if total_letters > 0:
        vowel_percentage = (vowel_count / total_letters) * 100
        consonant_percentage = (consonant_count / total_letters) * 100
        print(f"Процент гласных букв: {vowel_percentage:.2f}%")
        print(f"Процент согласных букв: {consonant_percentage:.2f}%")
    else:
        print("Слово не содержит букв.")

print("Программа завершена.")