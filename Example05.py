"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

with open("Example05.txt", "w") as text_file:
    r_num = [3, 4, 5, 1, 7, 2, 7]
    for i in range(0, len(r_num)):
        new_str = str(r_num[i]) + " "
        text_file.writelines(new_str)

with open("Example05.txt", "r") as text_file:
    line = text_file.read()
    line = line.split()
    sum = 0
    for i in line:
        sum = sum + int(i)
    print(f"Сумма чисел, записанных в файл, равна: {sum}")
