def linux_distro_selector():
    # Список дистрибутивов и их начальные очки
    distros = {
        "Ubuntu": 0,
        "Linux Mint": 0,
        "Fedora": 0,
        "Debian": 0,
        "Arch Linux": 0,
        "OpenSUSE": 0,
        "Manjaro": 0,
        "Alpine": 0,
        "Tails": 0,
        "Pop!_OS": 0,
    }


    # 1. Уровень сложности
    print("\n1. Как долго ты работаешь с Linux?")
    print("   a) менее года")
    print("   b) 1-3 года")
    print("   c) более 3 лет")
    experience_level = input("Выбери вариант (a/b/c): ").lower()
    while experience_level not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуй ещё раз.")
        experience_level = input("Выбери вариант (a/b/c): ").lower()
    if experience_level == "a":
        distros["Ubuntu"] += 3
        distros["Linux Mint"] += 3
        distros["Pop!_OS"] += 3
    elif experience_level == "b":
        distros["Ubuntu"] += 2
        distros["Fedora"] += 2
        distros["Debian"] += 2
        distros["OpenSUSE"] += 2
    elif experience_level == "c":
        distros["Arch Linux"] += 3
        distros["Debian"] += 2
        distros["Fedora"] += 2

    # 2. Поддержка оборудования
    print("\n2. Насколько важна поддержка оборудования?")
    print("   a) Необходимо")
    print("   b) Важно")
    print("   c) Не важно")
    hardware_support = input("Выбери вариант (a/b/c): ").lower()
    while hardware_support not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуй ещё раз.")
        hardware_support = input("Выбери вариант (a/b/c): ").lower()
    if hardware_support == "a":
        distros["Ubuntu"] += 3
        distros["Pop!_OS"] += 3
        distros["Manjaro"] += 3
    elif hardware_support == "b":
        distros["Fedora"] += 2
        distros["Debian"] += 2
        distros["OpenSUSE"] += 2
    elif hardware_support == "c":
        distros["Arch Linux"] += 1
        distros["Alpine"] += 1

    # 3. Целевое использование
    print("\n3. Для каких целей ты планируешь использовать дистрибутив?")
    print("   a) Десктоп (повседневное использование)")
    print("   b) Сервер")
    print("   c) Разработка ПО")
    print("   d) Мультимедиа (графика, видео, музыка)")
    print("   e) Приватность и анонимность")
    usage_purpose = input("Выбери вариант (a/b/c/d/e): ").lower()
    while usage_purpose not in ["a", "b", "c", "d", "e"]:
        print("Некорректный ввод. Попробуй ещё раз.")
        usage_purpose = input("Выбери вариант (a/b/c/d/e): ").lower()
    if usage_purpose == "a":
        distros["Ubuntu"] += 3
        distros["Linux Mint"] += 3
        distros["Pop!_OS"] += 3
    elif usage_purpose == "b":
        distros["Debian"] += 3
        distros["OpenSUSE"] += 3
        distros["Alpine"] += 3
    elif usage_purpose == "c":
        distros["Fedora"] += 3
        distros["Arch Linux"] += 3
        distros["OpenSUSE"] += 3
    elif usage_purpose == "d":
        distros["Ubuntu"] += 2
        distros["Fedora"] += 2
        distros["Manjaro"] += 2
    elif usage_purpose == "e":
        distros["Tails"] += 3
        distros["Debian"] += 2

    # 4. Модель выпуска обновлений
    print("\n4. Какую модель обновлений ты предпочитаешь?")
    print("   a) Rolling Release (постоянные обновления)")
    print("   b) Фиксированные релизы (стабильные версии)")
    update_model = input("Выбери вариант (a/b): ").lower()
    while update_model not in ["a", "b"]:
        print("Некорректный ввод. Попробуй ещё раз.")
        update_model = input("Выбери вариант (a/b): ").lower()
    if update_model == "a":
        distros["Arch Linux"] += 3
        distros["Manjaro"] += 3
        distros["Fedora"] += 2
    elif update_model == "b":
        distros["Ubuntu"] += 3
        distros["Debian"] += 3
        distros["OpenSUSE"] += 3

    # 5. Сообщество и поддержка
    print("\n5. Насколько важна поддержка сообщества и документация?")
    print("   a) Необходимо")
    print("   b) Важно")
    print("   c) Не важно")
    community_support = input("Выбери вариант (a/b/c): ").lower()
    while community_support not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуй ещё раз.")
        community_support = input("Выбери вариант (a/b/c): ").lower()
    if community_support == "a":
        distros["Ubuntu"] += 3
        distros["Fedora"] += 3
        distros["Debian"] += 3
    elif community_support == "b":
        distros["Linux Mint"] += 2
        distros["OpenSUSE"] += 2
    elif community_support == "c":
        distros["Arch Linux"] += 1
        distros["Alpine"] += 1

    # 6. Программное обеспечение из коробки
    print("\n6. Насколько важно наличие предустановленного ПО?")
    print("   a) Необходимо")
    print("   b) Важно")
    print("   c) Не важно")
    preinstalled_software = input("Выбери вариант (a/b/c): ").lower()
    while preinstalled_software not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуй ещё раз.")
        preinstalled_software = input("Выбери вариант (a/b/c): ").lower()
    if preinstalled_software == "a":
        distros["Ubuntu"] += 3
        distros["Linux Mint"] += 3
        distros["Pop!_OS"] += 3
    elif preinstalled_software == "b":
        distros["Fedora"] += 2
        distros["Manjaro"] += 2
    elif preinstalled_software == "c":
        distros["Arch Linux"] += 1
        distros["Debian"] += 1

    # 7. Безопасность и конфиденциальность
    print("\n7. Насколько важна безопасность и конфиденциальность?")
    print("   a) Необходимо")
    print("   b) Важно")
    print("   c) Не важно") 
    security_level = input("Выбери вариант (a/b/c): ").lower()
    while security_level not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуй ещё раз.")
        security_level = input("Выбери вариант (a/b/c): ").lower()
    if security_level == "a":
        distros["Tails"] += 3
        distros["Fedora"] += 2
        distros["Debian"] += 2
    elif security_level == "b":
        distros["Ubuntu"] += 1
        distros["OpenSUSE"] += 1
    elif security_level == "c":
        distros["Arch Linux"] += 0

    # 8. Производительность
    print("\n8. Насколько важна производительность на слабом оборудовании?")
    print("   a) Необходимо")
    print("   b) Важно")
    print("   c) Не важно")
    performance = input("Выбери вариант (a/b/c): ").lower()
    while performance not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуй ещё раз.")
        performance = input("Выбери вариант (a/b/c): ").lower()
    if performance == "a":
        distros["Alpine"] += 3
        distros["Arch Linux"] += 2
        distros["Manjaro"] += 2
    elif performance == "b":
        distros["Ubuntu"] += 1
        distros["Debian"] += 1
    elif performance == "c":
        distros["Fedora"] += 0

    # 9. Совместимость с проприетарным ПО
    print("\n9. Насколько важна совместимость с проприетарным ПО (Steam, Adobe, MS Office)?")
    print("   a) Необходимо")
    print("   b) Важно")
    print("   c) Не важно")
    proprietary_software = input("Выбери вариант (a/b/c): ").lower()
    while proprietary_software not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуй ещё раз.")
        proprietary_software = input("Выбери вариант (a/b/c): ").lower()
    if proprietary_software == "a":
        distros["Ubuntu"] += 3
        distros["Pop!_OS"] += 3
        distros["Manjaro"] += 2
    elif proprietary_software == "b":
        distros["Fedora"] += 1
        distros["OpenSUSE"] += 1
    elif proprietary_software == "c":
        distros["Debian"] += 0

    # 10. Локализация и языковая поддержка
    print("\n10. Насколько важна локализация и языковая поддержка?")
    print("   a) Необходимо")
    print("   b) Важно")
    print("   c) Не важно")
    localization = input("Выбери вариант (a/b/c): ").lower()
    while localization not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуй ещё раз.")
        localization = input("Выбери вариант (a/b/c): ").lower()
    if localization == "a":
        distros["Ubuntu"] += 2
        distros["Fedora"] += 2
        distros["Debian"] += 2
    elif localization == "b":
        distros["Linux Mint"] += 1
        distros["OpenSUSE"] += 1
    elif localization == "c":
        distros["Arch Linux"] += 0

    # Вывод результата
    print("\nРезультаты:")
    for distro, score in sorted(distros.items(), key=lambda item: item[1], reverse=True):
        print(f"{distro}: {score} очков")

    best_distro = max(distros, key=distros.get)
    print(f"\nРекомендуемый дистрибутив: {best_distro}")

linux_distro_selector()
