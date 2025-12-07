def level_1():
    text = "прИаЕт МИР"
    print(f"\nУровень 1: {text}")
    print("Доступные методы: upper, lower, capitalize")
    method = input("Введите метод: ").strip()

    if method == "upper":
        result = text.upper()
    elif method == "lower":
        result = text.lower()
    elif method == "capitalize":
        result = text.capitalize()
    else:
        print("Неверный метод!")
        return

    print(f"{text} {method} = {result}")


def level_2():
    text = "Ботать — это круто. Очень круто!"
    print(f"\nУровень 2: {text}")
    print("Доступные методы: find, replace, count")
    method = input("Введите метод: ").strip()

    if method == "find":
        substring = input("Введите подстроку для поиска: ")
        result = text.find(substring)
    elif method == "replace":
        old = input("Что заменить? ")
        new = input("На что заменить? ")
        result = text.replace(old, new)
    elif method == "count":
        char = input("Какой символ считать? ")
        result = text.count(char)
    else:
        print("Неверный метод!")
        return

    print(f"{text} {method} = {result}")


def level_3():
    text = "1,2,3,4,5,6"
    print(f"\nУровень 3: {text}")
    print("Доступные методы: split, join")
    method = input("Введите метод: ").strip()

    if method == "split":
        separator = input("По какому символу разделить? ")
        result = text.split(separator)
    elif method == "join":
        separator = input("Каким символом соединить? ")
        parts = text.split(',')
        result = separator.join(parts)
    else:
        print("Неверный метод!")
        return

    print(f"{text} {method} = {result}")


def level_4():
    text_a = "123456"
    text_b = "abc"
    text_c = " abc&* "
    print(f"\nУровень 4:")
    print("Доступные строки: text_a, text_b, text_c")
    print("Доступные методы: isdigit, isalpha, strip")

    text_choice = input("Выберите строку (a/b/c): ").strip().lower()
    if text_choice == 'a':
        text = text_a
    elif text_choice == 'b':
        text = text_b
    elif text_choice == 'c':
        text = text_c
    else:
        print("Неверная строка!")
        return

    method = input("Введите метод: ").strip()

    if method == "isdigit":
        result = text.isdigit()
    elif method == "isalpha":
        result = text.isalpha()
    elif method == "strip":
        result = text.strip()
    else:
        print("Неверный метод!")
        return

    print(f"{text} {method} = {result}")


def level_5():
    text_5 = "   python;IS;AWESomE!   "
    print("\nУровень 5:")
    stripped = text_5.strip()
    parts = stripped.split(';')
    first = parts[0].capitalize()
    second = parts[1].lower()
    third = parts[2][:-1].lower()
    result = f"{first} {second} {third}!"
    print("Результат:", result)


def main():
    print("Добро пожаловать в игру 'Строчник'!")
    print("На каждом уровне выберите метод и примените его к строке.")

    while True:
        level = input("Выберите уровень (1-5) или 'q' для выхода: ").strip()

        if level == 'q':
            print("Спасибо за игру!")
            break
        elif level == '1':
            level_1()
        elif level == '2':
            level_2()
        elif level == '3':
            level_3()
        elif level == '4':
            level_4()
        elif level == '5':
            level_5()
        else:
            print("Неверный уровень. Выберите 1-5 или 'q'.")


if __name__ == "__main__":
    main()
