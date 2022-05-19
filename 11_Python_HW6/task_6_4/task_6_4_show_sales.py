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
# запуск скрипта с двумя числами — выводить записи, начиная от номера, равного первому числу,
# по номер, равный второму числу, включительно; Если второе число больше, чем количество записей в файле - просто выводить до конца.
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

args_list = sys.argv
#args_list = ['task_6_4_show_sales.py', '4' ]       #  string used for debugging

if len(args_list) == 1:
    with open(file="bakery.csv", mode="rt", encoding="utf-8") as file_account:
        for el in file_account:
            print(el.strip())
    exit()
if len(args_list) == 2:
    try:
        start_line_num = int(args_list[1])
    except ValueError:
        print('\n  Please enter integer value as an argument')
        exit()
    with open(file="bakery.csv", mode="rt", encoding="utf-8") as file_account:
        i = 1
        while True:
            profit_amount=file_account.readline().strip()
            if profit_amount == '':
                break
            if i >= start_line_num:
                print(profit_amount)
            i +=1

if len(args_list) == 3:
    try:
        start_line_num = int(args_list[1])
    except ValueError:
        print('\n  Please enter integer value as an argument')
        exit()
    try:
        end_line_num = int(args_list[2])
    except ValueError:
        print('\n  Please enter integer value as an argument')
        exit()
    if start_line_num > end_line_num:
        print('\n  Please enter correct arguments')
    with open(file="bakery.csv", mode="rt", encoding="utf-8") as file_account:
        i=1
        while True:
            profit_amount = file_account.readline().strip()
            if profit_amount == '':
                break
            if start_line_num <= i <= end_line_num:
                print(profit_amount)
            i +=1

if len(args_list) > 3:
    print('\n please enter 1 or 2 arguments')



