"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

# Программа по замене числительных в текстовом файле с записью в новый файл

# Функция заменяет английские числительные в строке на русские
def multiple_replace(replaced_str, replace_values):
    """
    :param replaced_str: исходная строка для замены
    :param replace_values: словарь с соответствием русских числительных английским для замены
    :return replaced_str: строка с замененными числительными
    """
    for i, j in replace_values.items():
        # меняем все target_str на подставляемое
        replaced_str = replaced_str.replace(i, j)
    return replaced_str

# Здесь происходит открытие файла с исходным текстом,
with open("Example04.txt", encoding = "utf-8") as my_file:

    # а также открытие файла для записи текста с замененными числительными
    with open("New_example04.txt", "w", encoding="utf-8") as new_file:
        # Последовательно считываем строки из исходного текстового файла, заменям числительные
        # и записываем результат в новый файл
        for line in my_file:
            s_line = line.split()
            wr_line = s_line[0] + " " + s_line[1] + " " + s_line[2]
            replace_values = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
            new_line = multiple_replace(wr_line, replace_values)
            new_file.writelines(new_line + '\n')
            print(new_line)





