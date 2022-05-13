# 4. Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных.
#
# Техническое задание
#
# Все файлы этого задания хранить в отдельной директории, например «task_4» или на ваш выбор.
# Данные хранить в файле bakery.csv в кодировке utf-8.
# Соблюдаем формат данных в файле: одна запись (цифра) это одна строка.
# Для простоты все суммы продаж - целые числа.
# Запись в файл новых данных:
# Имя исполняемого скрипта: task_4_add_sale.py
# При записи передавать из командной строки значение суммы продаж. Функцию input не использовать.
# Новая запись дозаписывается в конец файла.
# Корректно обработать неправильное количество или тип переданных параметров.
# Вывод на экран записей:
# Имя исполняемого скрипта: task_4_show_sales.py
# Предполагаем, что первая запись имеет номер 1.
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи от номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная от номера, равного первому числу, по номер, равный второму числу, включительно;
# Если второе число больше, чем количество записей в файле - просто выводить до конца.
# Корректно обработать неправильное количество или тип переданных параметров.
# Примеры/Тесты:
# Примеры запуска скриптов:
#
#
# python add_sale.py 5978
# python add_sale.py 891
# python add_sale.py 7879
# python add_sale.py 1573
# python show_sales.py
# 5978
# 891
# 7879
# 1573
# python show_sales.py 3
# 7879
# 1573
# python show_sales.py 1 3
# 5978
# 891
# 7879
#
# Усложнение Подумать, как избежать чтения всего файла в память при реализации чтения данных в пунктах 4 и 5.

import sys

def if_end_is_lf(file_name):
# chrch if file ends with <LF>
    with open(file=file_name, mode="a+b") as file1:
        file1.seek(-1, 2)
        char1 = file1.read(1)
        if char1 == b'\n':
            # print ('True')
            return True
        else:
            # print ('False')
            return False

arguments=sys.argv
# arguments =['file', '3434' ]              # the line is using for debugging

if len(arguments) == 1:
    print('\n  Please provide a value to add')
    exit()

if len(arguments) >= 3:
    print('\n  Please provide a single value to add')
    exit()
try:
    value = int(arguments[1])
except ValueError:
    print('\n  Please enter integer value as an argument')
    exit()

if if_end_is_lf("bakery.csv"):
    string_to_add  = f'{value}\n'
else:
    string_to_add  = f'\n{value}'

with open(file="bakery.csv", mode= "at", encoding="utf-8") as file_account:
    file_account.write(string_to_add)

print('\n Value added to file')

