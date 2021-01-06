"""
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

new_file = open(r"Example01.txt", "w")
while True:
    y = True
    n = False
    if new_file.writable():
        user_data = input("Введите строку для записи в файл: ")
        new_file.write(user_data + '\n')
        print("\n")
        choise = input("Хотите ввести еще строку? y/n: ")
        if choise == 'y':
            continue
        elif choise == 'n':
            break
        else:
            print("Вы ввели неверный символ. Для продолжения ввода строк введите y, для завершения работы - n ")
    else:
        print("Нет доступа к файлу на запись")

new_file.close()