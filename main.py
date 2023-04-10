"""Pig-latin translator"""

def main():
    """

    :rtype: object
    """
    print("Проект \"Поросячья\" латынь'\n")

    vowel = ('e', 'y', 'u', 'i', 'o', 'a')

    while True:

        word = input("Введите слово\n")
        # сравниваем первый символ с vowel
        if word[0].lower() in vowel:
            # конкатенируем слово с указазанным звуком
            print(word.lower() + 'way')
        else:
            # в переменную first_letter кладем 1-й символ слова
            # делаем срез слова со второго символа и конкатенируем
            # переменную first_letter окончание
            first_letter = word[0].lower()
            print(word[1:] + first_letter + 'ay')

        try_again = input(("\n\nTry again? (Press Enter else n to quit)\n "))

        if try_again.lower() == "n":
            break


if __name__ == "__main__":
    main()
