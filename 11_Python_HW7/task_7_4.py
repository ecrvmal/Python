# 4. Написать скрипт, который для заданной папки выводит статистику размеров файлов
# Техническое задание
#
# Директорию с файлами 'some_data' можно скачать из прикрепленных к уроку файлов.
# Результат формируется в виде словаря
# ключи — верхняя граница размера файла.
# значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0)
# Границы диапазонов размеров считаем фиксированными данными - пусть будет кратна 10, как в примере.
# Программа должна легко модифицироваться под другие границы диапазонов.
# Программа должна легко модифицироваться под увеличение количества диапазонов.
# Т.е. если диапазонов станет 150 шутк - не надо будет переписывать всю программу.
# Формат вывода результата:
#
#
# {
#   100: 15,
#   1000: 3,
#   10000: 7,
#   100000: 2
# }
#
# Примечание:
#
# В примере: Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...

import os, time, winsound
from random import uniform


def funny_typing(string1):
    frequency = 5000
    duration = 10
    for ch in string1:
        time.sleep(uniform(0, 0.1))
        winsound.Beep(frequency, duration)
        print(ch, end='')
    print()                     # line feed

def size_diapazon(f_size, increment=10):
    if f_size == 0:
        min_value = 0
        max_value = 0
    elif 0 < f_size <= 1:
        min_value = 0
        max_value = 1
    else:
        min_value = 0
        max_value = 0
        i = 0
        while True:
            min_value = increment ** i
            max_value = increment ** (i + 1)
            if min_value < f_size <= max_value:
                break
            else:
                i += 1
                pass
    result = (min_value, max_value)
    return result


increment = 10
statistics = {}


current_path = os.getcwd()
target_path = os.path.join(current_path, 'task_7_4', 'some_data')
if not os.path.exists(target_path) or not os.path.isdir(target_path):
    print(f" Folder doesn't exist: {target_path} ")
j = 0
with os.scandir(target_path) as item:
    for entry in item:
        if not entry.name.startswith('.') and entry.is_file():
            size1 = entry.stat().st_size
            name1 = entry.name
            # j +=1
            # print(j, name1 , size1 )

            # calculating diapazon
            key_min_value , key_max_value = size_diapazon (size1 )

            # print ('defined key_min, key_max')
            # print(f'name1 = {name1}, size1 = {size1} ,key_min = {key_min_value} , key_max = {key_max_value} ')
            # Check if keys exists in dictionary :
            if not key_min_value in statistics.keys():
                statistics[key_min_value] = 0
                # print ('added key_min')
            if not key_max_value in statistics.keys():
                statistics[key_max_value] = 0
                # print ('added key_max')
            statistics[key_max_value] += 1
            # print('Increased statisics')
            # print(statistics)                 # print statistics dict after checking file.
        # print('pass1')
        pass
    # print('pass2')
    pass


funny_typing(f'\n  I CALCULATED STATISTICS AND ...')
funny_typing(f' AND NOW STATISTICS IS :  ')
print('{')
for key in (sorted(statistics.keys())[:-1]):
    statistics_string= f'    {key} : {statistics[key]} ,'
    funny_typing(statistics_string)
for key in (sorted(statistics.keys())[-1:]):
    statistics_string = f'    {key} : {statistics[key]} '
    funny_typing(statistics_string)
print('}')






