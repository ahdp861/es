def linux_distro_selector():

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

    q1 = input("1. Как давно вы работаете с Linux?\n"
               "   a) Меньше года\n"
               "   b) 1-3 года\n"
               "   c) Более 3 лет\n"
               "   d) Более 10 лет\n"
               "Ваш ответ: ").lower()
    while q1 not in ["a", "b", "c", "d"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q1 = input("Ваш ответ: ").lower()
    if q1 == "a":
        distros["Ubuntu"] += 2
        distros["Linux Mint"] += 2
        distros["Pop!_OS"] += 1
    elif q1 == "b":
        distros["Ubuntu"] += 1
        distros["Fedora"] += 1
        distros["Debian"] += 1
        distros["OpenSUSE"] += 1
    elif q1 == "c":
        distros["Arch Linux"] += 1
        distros["Debian"] += 1
        distros["Fedora"] += 1
    elif q1 == "d":
        distros["Arch Linux"] += 2
        distros["Debian"] += 2
        distros["Alpine"] += 1

    q2 = input("\n2. Как вы относитесь к использованию командной строки?\n"
               "   a) Стараюсь избегать, предпочитаю графический интерфейс\n"
               "   b) Использую иногда для простых команд\n"
               "   c) Часто использую, чувствую себя уверенно\n"
               "   d) Предпочитаю полностью работать в терминале\n"
               "Ваш ответ: ").lower()
    while q2 not in ["a", "b", "c", "d"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q2 = input("Ваш ответ: ").lower()
    if q2 == "a":
        distros["Ubuntu"] += 2
        distros["Linux Mint"] += 2
        distros["Pop!_OS"] += 2
    elif q2 == "b":
        distros["Ubuntu"] += 1
        distros["Manjaro"] += 1
        distros["OpenSUSE"] += 1
    elif q2 == "c":
        distros["Fedora"] += 1
        distros["Debian"] += 1
        distros["Arch Linux"] += 1
    elif q2 == "d":
        distros["Arch Linux"] += 2
        distros["Alpine"] += 1
        distros["Debian"] += 1

    q3 = input("\n3. Приходилось ли вам редактировать конфигурационные файлы вручную?\n"
               "   a) Нет, никогда\n"
               "   b) Да, но только по инструкциям\n"
               "   c) Да, регулярно\n"
               "Ваш ответ: ").lower()
    while q3 not in ["a", "b", "c", "d"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q3 = input("Ваш ответ: ").lower()
    if q3 == "a":
        distros["Ubuntu"] += 2
        distros["Linux Mint"] += 2
    elif q3 == "b":
        distros["Ubuntu"] += 1
        distros["Manjaro"] += 1
        distros["Fedora"] += 1
    elif q3 == "c":
        distros["Arch Linux"] += 1
        distros["Debian"] += 1
        distros["OpenSUSE"] += 1

    q4 = input("\n4. Приходилось ли вам собирать ядро или компилировать программы из исходников?\n"
               "   a) Нет, никогда\n"
               "   b) Да, но только по готовым инструкциям\n"
               "   c) Да, регулярно\n"
               "Ваш ответ: ").lower()
    while q4 not in ["a", "b", "c", "d"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q4 = input("Ваш ответ: ").lower()
    if q4 == "a":
        distros["Ubuntu"] += 2
        distros["Linux Mint"] += 1
        distros["Pop!_OS"] += 1
    elif q4 == "b":
        distros["Ubuntu"] += 1
        distros["Manjaro"] += 1
        distros["Fedora"] += 1
    elif q4 == "c":
        distros["Arch Linux"] += 1
        distros["Debian"] += 1
        distros["Alpine"] += 1

    q5 = input("\n5. Важно ли, чтобы все устройства (Wi-Fi, видео, принтер) работали сразу после установки?\n"
               "   a) Да, критически важно\n"
               "   b) Желательно, но готов к настройке\n"
               "   c) Не важно, могу настроить сам\n"
               "Ваш ответ: ").lower()
    while q5 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q5 = input("Ваш ответ: ").lower()
    if q5 == "a":
        distros["Ubuntu"] += 2
        distros["Linux Mint"] += 2
        distros["Pop!_OS"] += 2
    elif q5 == "b":
        distros["Fedora"] += 1
        distros["Debian"] += 1
        distros["OpenSUSE"] += 1
    elif q5 == "c":
        distros["Arch Linux"] += 1
        distros["Alpine"] += 1

    q6 = input("\n6. Используете ли вы новое оборудование?\n"
               "   a) Да, у меня новое видеокарта/процессор\n"
               "   b) Использую стандартное оборудование\n"
               "   c) У меня старое оборудование (старше 5 лет)\n"
               "Ваш ответ: ").lower()
    while q6 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q6 = input("Ваш ответ: ").lower()
    if q6 == "a":
        distros["Ubuntu"] += 1
        distros["Pop!_OS"] += 2
        distros["Manjaro"] += 1
        distros["Fedora"] += 1
    elif q6 == "b":
        distros["Ubuntu"] += 1
        distros["Linux Mint"] += 1
        distros["Debian"] += 1
    elif q6 == "c":
        distros["Alpine"] += 2
        distros["Arch Linux"] += 1
        distros["Manjaro"] += 1

    q7 = input("\n7. Готовы ли вы самостоятельно искать и устанавливать драйверы?\n"
               "   a) Нет, хочу чтобы всё работало из коробки\n"
               "   b) Да, если есть понятные инструкции\n"
               "   c) Да, я опытный в этом вопросе\n"
               "Ваш ответ: ").lower()
    while q7 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q7 = input("Ваш ответ: ").lower()
    if q7 == "a":
        distros["Ubuntu"] += 2
        distros["Linux Mint"] += 2
        distros["Pop!_OS"] += 2
    elif q7 == "b":
        distros["Ubuntu"] += 1
        distros["Manjaro"] += 1
        distros["Fedora"] += 1
    elif q7 == "c":
        distros["Arch Linux"] += 2
        distros["Debian"] += 2

    q8 = input("\n8. Будете ли вы использовать систему для повседневных задач (интернет, офис, фильмы)?\n"
               "   a) Да, это основной сценарий\n"
               "   b) Иногда\n"
               "   c) Нет\n"
               "Ваш ответ: ").lower()
    while q8 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q8 = input("Ваш ответ: ").lower()
    if q8 == "a":
        distros["Ubuntu"] += 2
        distros["Linux Mint"] += 2
        distros["Pop!_OS"] += 1
    elif q8 == "b":
        distros["Ubuntu"] += 1
        distros["Manjaro"] += 1

    q9 = input("\n9. Планируете ли вы использовать систему как сервер (веб-сервер, базы данных, файловое хранилище)?\n"
               "   a) Да, основной сценарий\n"
               "   b) Возможно, для личных проектов\n"
               "   c) Нет\n"
               "Ваш ответ: ").lower()
    while q9 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q9 = input("Ваш ответ: ").lower()
    if q9 == "a":
        distros["Debian"] += 3
        distros["Alpine"] += 3
        distros["OpenSUSE"] += 2
    elif q9 == "b":
        distros["Ubuntu"] += 1
        distros["Debian"] += 1
        distros["Fedora"] += 1

    q10 = input("\n10. Будете ли вы заниматься разработкой ПО или DevOps?\n"
                "   a) Да, профессионально\n"
                "   b) Да, в учебных целях\n"
                "   c) Нет\n"
                "Ваш ответ: ").lower()
    while q10 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q10 = input("Ваш ответ: ").lower()
    if q10 == "a":
        distros["Fedora"] += 2
        distros["Arch Linux"] += 2
        distros["OpenSUSE"] += 2
        distros["Ubuntu"] += 1
    elif q10 == "b":
        distros["Ubuntu"] += 1
        distros["Pop!_OS"] += 1
        distros["Manjaro"] += 1

    q11 = input("\n11. Планируете ли вы работать с мультимедиа (графика, видео, музыка)?\n"
                "   a) Да, профессионально\n"
                "   b) Да, как хобби\n"
                "   c) Нет\n"
                "Ваш ответ: ").lower()
    while q11 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q11 = input("Ваш ответ: ").lower()
    if q11 == "a":
        distros["Ubuntu"] += 2
        distros["Fedora"] += 2
        distros["Pop!_OS"] += 1
    elif q11 == "b":
        distros["Ubuntu"] += 1
        distros["Manjaro"] += 1
        distros["Linux Mint"] += 1

    q12 = input("\n12. Важна ли для вас анонимность и конфиденциальность в интернете?\n"
                "   a) Да, критически важно\n"
                "   b) Важно, но не критично\n"
                "   c) Не важно\n"
                "Ваш ответ: ").lower()
    while q12 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q12 = input("Ваш ответ: ").lower()
    if q12 == "a":
        distros["Tails"] += 3
        distros["Debian"] += 2
        distros["Alpine"] += 1
    elif q12 == "b":
        distros["Ubuntu"] += 1
        distros["Fedora"] += 1

    q13 = input("\n13. Как вы относитесь к частым обновлениям системы?\n"
                "   a) Радует, хочу всегда свежие версии\n"
                "   b) Нормально, если они не ломают систему\n"
                "   c) Раздражают, предпочитаю стабильность\n"
                "Ваш ответ: ").lower()
    while q13 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q13 = input("Ваш ответ: ").lower()
    if q13 == "a":
        distros["Arch Linux"] += 2
        distros["Manjaro"] += 2
        distros["Fedora"] += 1
    elif q13 == "b":
        distros["Ubuntu"] += 1
        distros["Fedora"] += 1
    elif q13 == "c":
        distros["Debian"] += 2
        distros["OpenSUSE"] += 2

    q15 = input("\n14. Нужна ли вам длительная поддержка одной версии (например, 5 лет без смены версии)?\n"
                "   a) Да, очень важно\n"
                "   b) Желательно\n"
                "   c) Не важно\n"
                "Ваш ответ: ").lower()
    while q15 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q15 = input("Ваш ответ: ").lower()
    if q15 == "a":
        distros["Ubuntu"] += 2
        distros["Debian"] += 2
        distros["Linux Mint"] += 1
    elif q15 == "b":
        distros["Ubuntu"] += 1
        distros["OpenSUSE"] += 1

    q16 = input("\n15. Насколько важно наличие большого русскоязычного сообщества?\n"
                "   a) Очень важно, хочу спрашивать на русском\n"
                "   b) Важно, но могу читать английские форумы\n"
                "   c) Не важно\n"
                "Ваш ответ: ").lower()
    while q16 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q16 = input("Ваш ответ: ").lower()
    if q16 == "a":
        distros["Ubuntu"] += 2
        distros["Linux Mint"] += 2
        distros["Debian"] += 1
    elif q16 == "b":
        distros["Fedora"] += 1
        distros["Arch Linux"] += 1

    q17 = input("\n16. Пользуетесь ли вы официальной документацией?\n"
                "   a) Да, это основной источник информации\n"
                "   b) Иногда\n"
                "   c) Предпочитаю видеоуроки и статьи\n"
                "Ваш ответ: ").lower()
    while q17 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q17 = input("Ваш ответ: ").lower()
    if q17 == "a":
        distros["Debian"] += 1
        distros["Fedora"] += 1
        distros["Arch Linux"] += 1
    elif q17 == "b":
        distros["Ubuntu"] += 1
        distros["OpenSUSE"] += 1
    elif q17 == "c":
        distros["Ubuntu"] += 1
        distros["Linux Mint"] += 1
        distros["Manjaro"] += 1

    q18 = input("\n17. Как вы предпочитаете решать проблемы с системой?\n"
                "   a) Искать готовые решения на форумах/StackOverflow\n"
                "   b) Читать официальную документацию\n"
                "   c) Разбираться самостоятельно\n"
                "Ваш ответ: ").lower()
    while q18 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q18 = input("Ваш ответ: ").lower()
    if q18 == "a":
        distros["Ubuntu"] += 2
        distros["Linux Mint"] += 2
    elif q18 == "b":
        distros["Debian"] += 1
        distros["Fedora"] += 1
    elif q18 == "c":
        distros["Arch Linux"] += 2
        distros["Alpine"] += 1

    q19 = input("\n18. Хотите ли вы получить готовый к работе набор программ сразу после установки?\n"
                "   a) Да, полный набор\n"
                "   b) Достаточно базового набора\n"
                "   c) Нет, лучше минимальная система\n"
                "Ваш ответ: ").lower()
    while q19 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q19 = input("Ваш ответ: ").lower()
    if q19 == "a":
        distros["Ubuntu"] += 2
        distros["Linux Mint"] += 2
        distros["Pop!_OS"] += 2
    elif q19 == "b":
        distros["Fedora"] += 1
        distros["Manjaro"] += 1
    elif q19 == "c":
        distros["Arch Linux"] += 2
        distros["Alpine"] += 2
        distros["Debian"] += 1

    q20 = input("\n19. Насколько для вас важен графический интерфейс «из коробки»?\n"
                "   a) Очень важен\n"
                "   b) Важен\n"
                "   c) Не важен\n"
                "Ваш ответ: ").lower()
    while q20 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q20 = input("Ваш ответ: ").lower()
    if q20 == "a":
        distros["Ubuntu"] += 2
        distros["Linux Mint"] += 2
        distros["Pop!_OS"] += 1
    elif q20 == "b":
        distros["Fedora"] += 1
        distros["Manjaro"] += 1
    elif q20 == "c":
        distros["Arch Linux"] += 1
        distros["Debian"] += 1

    q21 = input("\n20. Нужны ли вам предустановленные мультимедийные кодеки и проприетарные драйверы?\n"
                "   a) Да, обязательно\n"
                "   b) Желательно\n"
                "   c) Не важно\n"
                "Ваш ответ: ").lower()
    while q21 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q21 = input("Ваш ответ: ").lower()
    if q21 == "a":
        distros["Ubuntu"] += 2
        distros["Linux Mint"] += 1
        distros["Pop!_OS"] += 1
    elif q21 == "b":
        distros["Manjaro"] += 1
        distros["Fedora"] += 1

    q22 = input("\n21. Насколько серьёзно вы относитесь к шифрованию данных?\n"
                "   a) Очень серьёзно, шифрую всё\n"
                "   b) Шифрую важные файлы\n"
                "   c) Не использую шифрование\n"
                "Ваш ответ: ").lower()
    while q22 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q22 = input("Ваш ответ: ").lower()
    if q22 == "a":
        distros["Tails"] += 2
        distros["Debian"] += 2
        distros["Alpine"] += 1
    elif q22 == "b":
        distros["Ubuntu"] += 1
        distros["Fedora"] += 1
        distros["OpenSUSE"] += 1

    q24 = input("\n22. Важно ли, чтобы система не собирала телеметрию и не отправляла данные разработчикам?\n"
                "   a) Да, критически важно\n"
                "   b) Важно\n"
                "   c) Не важно\n"
                "Ваш ответ: ").lower()
    while q24 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q24 = input("Ваш ответ: ").lower()
    if q24 == "a":
        distros["Tails"] += 2
        distros["Debian"] += 2
        distros["Alpine"] += 2
    elif q24 == "b":
        distros["Fedora"] += 1
        distros["OpenSUSE"] += 1

    q25 = input("\n23. Какой объём оперативной памяти у вашего компьютера?\n"
                "   a) Менее 2 ГБ\n"
                "   b) 2-4 ГБ\n"
                "   c) 4-8 ГБ\n"
                "   d) Более 8 ГБ\n"
                "Ваш ответ: ").lower()
    while q25 not in ["a", "b", "c", "d"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q25 = input("Ваш ответ: ").lower()
    if q25 == "a":
        distros["Alpine"] += 3
        distros["Arch Linux"] += 1
    elif q25 == "b":
        distros["Alpine"] += 2
        distros["Manjaro"] += 1
        distros["Linux Mint"] += 1
    elif q25 == "c":
        distros["Ubuntu"] += 1
        distros["Fedora"] += 1
        distros["Pop!_OS"] += 1
    elif q25 == "d":
        distros["Ubuntu"] += 1
        distros["Fedora"] += 1

    q26 = input("\n24. Готовы ли вы использовать лёгкие оконные менеджеры вместо тяжелых графических оболочек?\n"
                "   a) Да, без проблем\n"
                "   b) Возможно, но предпочитаю полноценный DE\n"
                "   c) Нет, нужен полный графический интерфейс\n"
                "Ваш ответ: ").lower()
    while q26 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q26 = input("Ваш ответ: ").lower()
    if q26 == "a":
        distros["Alpine"] += 2
        distros["Arch Linux"] += 2
    elif q26 == "b":
        distros["Manjaro"] += 1
        distros["Ubuntu"] += 1
    elif q26 == "c":
        distros["Ubuntu"] += 1
        distros["Linux Mint"] += 1
        distros["Pop!_OS"] += 1

    q27 = input("\n25. Планируете ли вы использовать систему на Raspberry Pi или другом маломощном устройстве?\n"
                "   a) Да\n"
                "   b) Возможно\n"
                "   c) Нет\n"
                "Ваш ответ: ").lower()
    while q27 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q27 = input("Ваш ответ: ").lower()
    if q27 == "a":
        distros["Alpine"] += 3
        distros["Debian"] += 2
    elif q27 == "b":
        distros["Ubuntu"] += 1


    q28 = input("\n26. Планируете ли вы устанавливать проприетарные драйверы для видеокарт NVIDIA или AMD?\n"
                "   a) Да, обязательно\n"
                "   b) Возможно\n"
                "   c) Нет, у меня встроенная графика\n"
                "Ваш ответ: ").lower()
    while q28 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q28 = input("Ваш ответ: ").lower()
    if q28 == "a":
        distros["Ubuntu"] += 2
        distros["Pop!_OS"] += 3
        distros["Manjaro"] += 2
    elif q28 == "b":
        distros["Ubuntu"] += 1
        distros["Fedora"] += 1

    q29 = input("\n27. Нужны ли вам коммерческие программы, такие как Adobe Photoshop, MS Office или игры в Steam?\n"
                "   a) Да, критически важно\n"
                "   b) Желательно\n"
                "   c) Не важно, использую открытые аналоги\n"
                "Ваш ответ: ").lower()
    while q29 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q29 = input("Ваш ответ: ").lower()
    if q29 == "a":
        distros["Ubuntu"] += 2
        distros["Pop!_OS"] += 2
        distros["Linux Mint"] += 1
    elif q29 == "b":
        distros["Manjaro"] += 1
        distros["Fedora"] += 1
    elif q29 == "c":
        distros["Debian"] += 1
        distros["Alpine"] += 1

    q31 = input("\n28. Насколько для вас важен полностью переведённый на русский язык интерфейс системы?\n"
                "   a) Очень важен, хочу всё на русском\n"
                "   b) Важен, но английский допускаю\n"
                "   c) Не важен, работаю на английском\n"
                "Ваш ответ: ").lower()
    while q31 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q31 = input("Ваш ответ: ").lower()
    if q31 == "a":
        distros["Ubuntu"] += 2
        distros["Linux Mint"] += 2
        distros["Fedora"] += 1
    elif q31 == "b":
        distros["Ubuntu"] += 1
        distros["OpenSUSE"] += 1
        distros["Manjaro"] += 1

    q34 = input("\n29. Важна ли для вас поддержка русской раскладки, словарей и локализованных меню?\n"
                "   a) Да, обязательно\n"
                "   b) Важно\n"
                "   c) Не важно\n"
                "Ваш ответ: ").lower()
    while q34 not in ["a", "b", "c"]:
        print("Некорректный ввод. Попробуйте ещё раз.")
        q34 = input("Ваш ответ: ").lower()
    if q34 == "a":
        distros["Ubuntu"] += 2
        distros["Linux Mint"] += 2
        distros["Fedora"] += 1
    elif q34 == "b":
        distros["OpenSUSE"] += 1
        distros["Manjaro"] += 1

    print("\nРейтинг дистрибутивов (по убыванию):")
    for distro, score in sorted(distros.items(), key=lambda item: item[1], reverse=True):
        if score > 0:
            bar = "█" * min(score, 15)
            print(f"{distro:12} : {score:2} очков  {bar}")
        else:
            print(f"{distro:12} : {score:2} очков")

    best_distro = max(distros, key=distros.get)
    best_score = distros[best_distro]

    print(f"РЕКОМЕНДУЕМЫЙ ДИСТРИБУТИВ: {best_distro}")
    print(f"   Количество баллов: {best_score}")



    tips = {
        "Ubuntu": "Отличный выбор для новичков и универсального использования. Огромное сообщество, лучшая локализация.",
        "Linux Mint": "Идеален для новичков, интерфейс похож на Windows. Отличная локализация и предустановленное ПО.",
        "Fedora": "Современный дистрибутив для разработчиков и опытных пользователей. Свежие технологии.",
        "Debian": "Максимальная стабильность. Выбор профессионалов и серверов. Отличная безопасность.",
        "Arch Linux": "Гибкость и контроль. Для опытных пользователей, любящих настройку. Rolling Release.",
        "OpenSUSE": "Мощный инструмент для системных администраторов и разработчиков. Отличная документация.",
        "Manjaro": "Простота Arch с удобной установкой. Хорош для игр и мультимедиа.",
        "Alpine": "Лёгкий и безопасный. Идеален для слабого оборудования и серверов. Минимализм.",
        "Tails": "Максимальная анонимность. Используйте для конфиденциальной работы. Безопасность превыше всего.",
        "Pop!_OS": "Оптимизирован для разработчиков и игр. Отличная поддержка NVIDIA и новейшего оборудования."
    }
    if best_distro in tips:
        print(f"\n{tips[best_distro]}")

if __name__ == "__main__":
    linux_distro_selector()