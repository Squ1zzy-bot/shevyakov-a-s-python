import random

# Начальные настройки
inventory = []  # инвентарь игрока
lives = 3       # жизни
has_key = False # есть ли ключ?
game_over = False

# Возможные комнаты
rooms = ["пусто", "сундук", "монстр", "ключ", "ловушка", "портал"]

print("Добро пожаловать в Лабиринт Списков!")
print("У вас есть 3 жизни. Инвентарь пуст.")
print("Вы не знаете, какая комната ждёт вас впереди...")

while lives > 0 and not game_over:
    print(f"\nЖизней: {lives}")
    print(f"Инвентарь: {inventory}")

    # Генерируем случайную комнату
    current_room = random.choice(rooms)
    print("\nВы подходите к двери... Что за ней? Неизвестно.")

    input("Нажмите Enter, чтобы войти в комнату...")

    # Обработка комнаты
    if current_room == "пусто":
        print("Вы вошли в пустую комнату. Здесь ничего нет.")
        print("Вы продолжаете путь.")

    elif current_room == "сундук":
        items = ["золото", "аптечка", "нож", "фонарик", "хлеб"]
        found_item = random.choice(items)
        print(f"Вы нашли сундук! Внутри: {found_item}")
        choice = input("Добавить в инвентарь? (да/нет): ").strip().lower()
        if choice == "да":
            inventory.append(found_item)
            print(f"{found_item} добавлен в инвентарь.")
        else:
            print("Вы оставили предмет.")

    elif current_room == "монстр":
        print("Вы встретили монстра!")
        if "нож" in inventory:
            print("У вас есть нож. Хотите сразиться?")
            choice = input("(да/нет): ").strip().lower()
            if choice == "да":
                print("Вы победили монстра!")
                inventory.remove("нож")
                print("Нож потерян, но вы живы.")
            else:
                print("Вы решили бежать... Монстр догнал вас!")
                lives -= 1
                print(f"Вы потеряли жизнь. Осталось: {lives}")
        else:
            print("Без ножа вы не справились...")
            lives -= 1
            print(f"Вы потеряли жизнь. Осталось: {lives}")

    elif current_room == "ключ":
        print("Вы нашли ключ!")
        inventory.append("ключ")
        has_key = True
        print("Ключ добавлен в инвентарь.")

    elif current_room == "ловушка":
        print("Вы попали в ловушку!")
        if "аптечка" in inventory:
            print("У вас есть аптечка. Использовать?")
            choice = input("(да/нет): ").strip().lower()
            if choice == "да":
                print("Вы выжили!")
                inventory.remove("аптечка")
                print("Аптечка использована.")
            else:
                print("Вы не использовали аптечку...")
                lives -= 1
                print(f"Вы потеряли жизнь. Осталось: {lives}")
        else:
            print("Без аптечки вы не выжили...")
            lives -= 1
            print(f"Вы потеряли жизнь. Осталось: {lives}")

    elif current_room == "портал":
        print("Вы нашли портал!")
        if has_key:
            print("У вас есть ключ! Вы открываете портал и выходите из лабиринта!")
            print("ПОБЕДА!")
            print(f"Ваш финальный инвентарь: {sorted(inventory)}")
            game_over = True
        else:
            print("Без ключа портал не открыть. Вы не можете выйти.")
            print("Вы остаётесь в лабиринте...")

    # Проверка конца игры
    if lives <= 0:
        print("\nВсе жизни потеряны. Игра окончена.")
        game_over = True

if not game_over:
    print("\nВы покинули лабиринт, но без победы... Попробуйте снова!")
