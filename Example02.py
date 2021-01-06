"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
# Программа подсчета количеств строк в файле и слов в каждой строке


with open('Example02.txt') as my_file:
    content = my_file.readlines()
    scount = len(content)
    print(f"В файле {scount} строки")

with open('Example02.txt') as my_file:
    i = 0
    for line in my_file:
        s_line = line.split()
        wcount = len(s_line)
        i += 1
        print(f"В {i}-ой строке {wcount} слов")



