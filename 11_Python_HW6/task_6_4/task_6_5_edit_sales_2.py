# 5. [Задача со звездочкой]: усложненный вариант задания 4.
# Добавить возможность редактирования данных при помощи отдельного скрипта.
# Техническое задание
#
# Скрипт получает два параметра: номер записи и новое значение
# Файл не должен считываться в память целиком. Обязательно.
# Не создавать дополнительных/«промежуточных» файлов
# Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует: ничего в файле не меняем, выводим сообщение в консоль.

 
import sys

args_list = sys.argv
#args_list = ['task_6_5show_sales.py', '6', '30']       #  string used for debugging

if len(args_list) != 3:
    print('\n  Please enter string number and value')
    exit()
try:
    line_num = int(args_list[1])
except ValueError:
    print('\n  Please enter integer value for line number')
    exit()
try:
    cash_amount = int(args_list[2])
except ValueError:
    print('\n  Please enter integer value as an cash amount')
    exit()

with open(file="bakery.csv", mode="r+t", encoding="utf-8") as file_account:
    for i in range(1,line_num):
        line1 = file_account.readline()

        if line1 == '':
            print('\n The string number out of file content \n')
            exit()


    pos1 = file_account.tell()
    next_line1 = file_account.readline()
    next_line2 = file_account.readline()
    file_account.seek(pos1)
    file_account.write(f'{cash_amount}\n')
    file_account.write(next_line1)
    pos1 = file_account.tell()
    next_line1= next_line2

    while True:
        pos1 = file_account.tell()
        next_line2 = file_account.readline()    # pass 1 line
        next_line2 = file_account.readline()    # Store 2-nd line
        file_account.seek(pos1)
        file_account.write(next_line1)
        next_line1 = next_line2
        if next_line1 == '':
            break

print('\n File has been owerwritten')





