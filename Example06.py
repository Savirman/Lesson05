"""Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""
"""
Программа считывает из файла расписание занятий, высчитывает общее количество часов занятий по предмету, 
формирует словарь из соответствий предмет - общее количество часов занятий, 
а затем выводит полученный словарь на экран
"""
# Открытие файла-расписания
with open("Example06.txt", encoding = "utf-8") as my_file:
    # Подсчет количества строк (необходимо для расчета часов для каждого предмета,
    # т.к. данные по одному предмету размещены в одной строке
    content = my_file.readlines()
    scount = len(content)
    schedule_dict = {}
    with open("Example06.txt", encoding="utf-8") as my_file:
        # Подготовка строки для нахождения часов занятий
        for line in range(0, scount):
            content = my_file.readline()
            content = content.split()

            # Подсчет общего количества часов занятий по каждому предмету
            sum = 0
            for el in content:
                q = "".join(i for i in el if i.isdigit())
                if q.isdigit():
                    sum = sum + int(q)

                    # Формирование словаря {предмет: количество часов}
                    subj_dict = {content[0]: sum}
            schedule_dict.update(subj_dict)
        print(schedule_dict)


