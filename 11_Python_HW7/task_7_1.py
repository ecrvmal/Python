# Тема урока: Работа с файлами и директориями: копирование, перемещение, создание, рекурсивный обход директории. Работа с Исключениями.
#
# Для всех заданий этого урока:
#
# Для каждой задачи создайте свою папку, например «task_1» и т.п., и в ней храните данные для этой задачи.
# Ваш код должен работать на любой ОС: не используйте в качестве путей строки с слешами.
# Ваш код должен корректно работать при «конфликтах» при создании файлов/директорий, т.е. если такие уже есть. Либо используйте соответствующие функции проверки/игнорирования конфликтов, либо явно обрабатывайте через try/except.
# Не забываем про методичку, материалы вебинара и советы на яндекс-диске
# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
#
# |--my_project
# |   |--settings
# |   |--mainapp
# |   |--adminapp
# |   |--authapp
#
# Техническое задание
#
# Продумайте ситуацию, когда все или часть этих папок уже есть в директории.
# Выберите наиболее подходящую структуру данных для хранения имен папок так, чтобы легко расширить количество создаваемых папок, например до 100 папок.
# Примечание:
#
# Можно ли будет расширять конфигурацию и хранить данные о вложенных папках и файлах?

import os


def dir_create_if_not_exists(dir_path_full):
    if not os.path.exists(dir_path_full) or not os.path.isdir(dir_path_full):
        os.mkdir(dir_path_full)
        print(f' Folder created : {dir_path_full} ')



#   relative paths to folders
dir_paths = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}

dir_current_full = os.getcwd()
dir_path_branch_full = os.path.join(dir_current_full, 'task_7_1')
dir_create_if_not_exists(dir_path_branch_full)

#path_1 =[]

#dir_level = 1
#path_1.append('')
for dir_name1_short in dir_paths.keys():
    pass
    dir_name1_full = os.path.join(dir_path_branch_full, dir_name1_short )
    # print('path_1 = ', dir_name1_full)
    dir_create_if_not_exists(dir_name1_full)
    # dir_level +=1
    for dir_name2_short in dir_paths[dir_name1_short]:
        dir_name2_full = os.path.join(dir_name1_full, dir_name2_short )
        dir_create_if_not_exists( dir_name2_full)
        # print('path_2 = ', dir_name2_full)


