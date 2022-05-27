# 5. [Задача со звездочкой]: усложненный вариант задания 4. Написать скрипт, который для заданной папки выводит статистику размеров файлов по расширениям.
# Техническое задание
#
# Директорию с файлами 'some_data_adv' можно скачать из прикрепленных к уроку файлов.
# Результат формируется в виде словаря
# ключи — верхняя граница размера файла (пусть будет кратна 10) - как в задании 4.
# значения — списки вида '[<files_quantity>, [<files_extensions_list>]]'. В список '<files_extensions_list>' заносятся все расширения для файлов удовлетворяющих условию размера, без повторений.
# Словарь сохраните в файл '<folder_name>_summary.json' в той же папке, где запустили скрипт.
# Формат вывода результата:
#
#
# {
#     100: [15, ['txt']],
#     1000: [3, ['py', 'txt']],
#     10000: [7, ['html', 'css']],
#     100000: [2, ['png', 'jpg']]
#   }

import os, time, winsound


def funny_typing(string1):
    frequency = 5000
    duration = 10
    for ch in string1:
        time.sleep(0.05)
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
target_path = os.path.join(current_path, 'task_7_5', 'some_data_adv')
if not os.path.exists(target_path) or not os.path.isdir(target_path):
    print(f" Folder doesn't exist: {target_path} ")
j = 0                                                   # the counter count line processed , it is for debug purposes
with os.scandir(target_path) as item:
    for entry in item:
        if not entry.name.startswith('.') and entry.is_file():
            size1 = entry.stat().st_size
            name1 = entry.name
            j += 1
            # print(j, name1 , size1 )                  # the debug printing for each file

            # calculating diapazon
            key_min_value, key_max_value = size_diapazon(size1)

            # print ('defined key_min, key_max')
            # print(f'name1 = {name1}, size1 = {size1} ,key_min = {key_min_value} , key_max = {key_max_value} ')
            # Check if keys exists in dictionary :
            if key_min_value not in statistics.keys():
                statistics[key_min_value] = [0, []]          # add item to dictionary with key ( min_size)
                # print ('added key_min')
            if key_max_value not in statistics.keys():
                statistics[key_max_value] = [0, []]          # add item to dictionary with key ( mmax_size)
                # print ('added key_max')
            statistics[key_max_value][0] += 1               #   increment  number of files
            file_ext = name1.split(".")[1]                    # file_extenson
            # print (f' ext = {file_ext}')                  #  print for debug purposes
            if file_ext in statistics[key_max_value][1]:    #   check if extension is in list already
                pass
            else:
                statistics[key_max_value][1].append(file_ext)       #  add new extension to list
            # print(statistics)                             # print statistics dict after checking each iten
        pass
    pass


funny_typing(f'\n  I CALCULATED STATISTICS AND ...')
funny_typing(f' AND NOW STATISTICS IS :  ')
print('{')
for key in (sorted(statistics.keys())[:-1]):                # print lines except the last one with , at the end
    print(f'    {key} : {statistics[key]} ,')
for key in (sorted(statistics.keys())[-1:]):
    print(f'    {key} : {statistics[key]} ')                # print last lines without , at the end
print('}')
