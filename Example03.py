"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32"""

with open('Example03.txt') as my_file:
    employees = len(my_file.readlines())

my_file = open("Example03.txt", "r", encoding = "utf-8")
i = 0
sum = 0

for line in my_file:
    s_line = line.split()
    oklad = int(s_line[i + 1])
    sum = (sum + oklad)
    if oklad < 20000:
        print(f"{s_line[i]} имеет оклад менее 20000")

sr_oklad = sum / employees
print(f"\nСредняя величина дохода сотрудников {sr_oklad} рублей")
my_file.close()