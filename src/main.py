#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Побег из заброшенной обсерватории — каркас (Вариант 2, лаб. №2).
# Без функций, списков, словарей, классов, импортов.

room = "dome"
has_lens = False
has_gear = False

print("Почините механизм купола и выйдите через exit.")
print("Команды: help, look, go <направление>, take <деталь>, use <деталь>, exit.")

# стартовый look
print("\n[dome] Главный купол обсерватории. Телескоп разбит, механизм заклинен.")
print("Предметы: —")
print("Выходы: library, basement")

while True:
    line = input("\n> ").strip().lower()
    if line == "":
        continue

    sp = line.find(" ")
    if sp == -1:
        cmd = line
        arg = ""
    else:
        cmd = line[:sp]
        arg = line[sp + 1:].strip()

    if cmd == "help":
        print("help, look, go <направление>, take <деталь>, use <деталь>, exit")

    elif cmd == "look":
        if room == "dome":
            print("[dome] Главный купол обсерватории. Телескоп разбит, механизм заклинен.")
            print("Предметы: —")
            print("Выходы: library, basement")
        elif room == "library":
            print("[library] Библиотека. Пыльные книги, шкаф с оптикой.")
            print("Предметы: lens")
            print("Выходы: dome, mechanic")
        elif room == "basement":
            print("[basement] Подвал. Ящики с запчастями, сырость.")
            print("Предметы: gear")
            print("Выходы: dome, mechanic")
        elif room == "mechanic":
            print("[mechanic] Механическая мастерская. Механизм купола и верстак.")
            print("Предметы: —")
            print("Выходы: library, basement, exit")
        elif room == "exit":
            print("[exit] Выход из обсерватории. Ночное небо.")
            print("Предметы: —")
            print("Выходы: mechanic")

    elif cmd == "go":
        ok = False
        if room == "dome" and (arg == "library" or arg == "basement"):
            ok = True
        elif room == "library" and (arg == "dome" or arg == "mechanic"):
            ok = True
        elif room == "basement" and (arg == "dome" or arg == "mechanic"):
            ok = True
        elif room == "mechanic" and (arg == "library" or arg == "basement" or arg == "exit"):
            ok = True
        elif room == "exit" and arg == "mechanic":
            ok = True

        if ok:
            room = arg
            print("Вы в комнате: " + room)
        else:
            print("Нет такого перехода.")

    elif cmd == "take":
        if arg == "lens" and room == "library" and not has_lens:
            has_lens = True
            print("Вы взяли lens (линзу).")
        elif arg == "lens" and room == "library":
            print("lens уже взят.")
        elif arg == "lens":
            print("lens находится в library.")
        elif arg == "gear" and room == "basement" and not has_gear:
            has_gear = True
            print("Вы взяли gear (шестерёнку).")
        elif arg == "gear" and room == "basement":
            print("gear уже взят.")
        elif arg == "gear":
            print("gear находится в basement.")
        else:
            print("Здесь нечего взять: '" + arg + "'.")

    elif cmd == "use":
        if arg == "mechanism" and room == "mechanic":
            if has_lens and has_gear:
                print("\n*** Победа! Механизм купола починен. Вы выходите через exit. ***")
                break
            else:
                missing = ""
                if not has_lens:
                    missing = "lens"
                if not has_gear:
                    if missing != "":
                        missing = missing + " и gear"
                    else:
                        missing = "gear"
                print("Для починки нужны обе детали. Не хватает: " + missing + ".")
        elif arg == "mechanism":
            print("Механизм находится в mechanic.")
        else:
            print("Здесь '" + arg + "' использовать нельзя.")

    elif cmd == "exit":
        if room == "exit":
            print("Сначала почините механизм купола в mechanic (use mechanism).")
        else:
            print("Выход находится в комнате exit. Доберитесь до mechanic → exit.")

    else:
        print("Неизвестная команда. Введите help.")
