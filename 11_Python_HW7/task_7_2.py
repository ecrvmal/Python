# 2. [Задача со звездочкой]: усложненный вариант задания 1.
# Написать скрипт, создающий из config_2.yaml стартер для проекта со следующей структурой:
#
# |--my_project
# |  |--settings
# |  |  |--__init__.py
# |  |  |--dev.py
# |  |  |--prod.py
# |  |--mainapp
# |  |  |--__init__.py
# |  |  |--models.py
# |  |  |--views.py
# |  |  |--templates
# |  |  |  |--mainapp
# |  |  |  |  |--base.html
# |  |  |  |  |--index.html
# |  |--authapp
# |  |  |--__init__.py
# |  |  |--models.py
# |  |  |--views.py
# |  |  |--templates
# |  |  |  |--authapp
# |  |  |  |  |--base.html
# |  |  |  |  |--index.html
#
# Техническое задание
#
# Пример файла config_2.yaml можно скачать из прикрепленных к уроку файлов.
# Или его можно создать в любом текстовом редакторе «руками» (не программно).
# Не используйте библиотеки для работы с YAML, проведите парсинг вручную.
#
# Правильный парсинг yaml - интересная задача, но может быть сложной.
# В этой задаче примем: глубина иерархии в директории определяется количеством пробелов;
# отличие директории о файла выберите сами: например в имени файла будет точка или после имени директории стоит двоеточие.
# Подумайте о возможных исключениях при работе скрипта.

import os


def dir_create_if_not_exists(dir_path_full):
    if not os.path.exists(dir_path_full) or not os.path.isdir(dir_path_full):
        os.mkdir(dir_path_full)
        print(f' Folder created         : {dir_path_full} ')
    else:
        print(f' Folder already exists  : {dir_path_full} ')

def file_create_if_not_exists(file_path_full, content):
    if not os.path.isfile(file_path_full):
        with open(file = file_path_full, mode = 'wt', encoding= 'utf-8') as new_file:
            new_file.write(content)
        print(f' File created           : {file_path_full} ')
    else:
        print(f' File already exists    : {file_path_full} ')

def line_analyze(stringline):
    #   print(stringline)                               #   this line is used for debugging purposes
    for i in range (len(stringline)):
        if stringline[i] ==' ':
           pass
        else:
            count_spaces = i
            break

    if stringline[-2] == ":":
        obj_type = 'dir'
    else:
        obj_type = 'file'
    for i in range (len(stringline)):
        if stringline[i] ==' ' or stringline[i] =='-':
            pass
        else:
            name_start = i
            break
    if obj_type == 'dir':
        obj_name = stringline[name_start:len(stringline)-2]
    else:
        obj_name = stringline[name_start:len(stringline)-1]
    result = (obj_type, obj_name, int(count_spaces /2) )
    return result

#   obj1, name1, spaces  = line_analyze("    - __init__.py")                #   this line is used for debugging purposes
#   print(f'obj = {obj1}, name = {name1}, level = {spaces}' )               #   this line is used for debugging purposes


dir_current_full = os.getcwd()
dir_path_branch_full_1 = os.path.join(dir_current_full, 'task_7_2')
dir_create_if_not_exists(dir_path_branch_full_1)

current_short_path =[]

with open(file = 'config_2.yaml', mode = 'rt' , encoding='utf-8') as config_file:
    for config_line in config_file:
        obj1, name1, dir_level = line_analyze(config_line)
        # print(f'obj = {obj1}, name = {name1}, level = {spaces}')          #   this line is used for debugging purposes

        if obj1 == 'dir':
            dir_path_branch_full_2=dir_path_branch_full_1
            if len(current_short_path) < dir_level+1:
                current_short_path.append(name1)                            #   add level to  list current_short_path
            else:
                current_short_path[dir_level]=name1                         #   update   list current_short_path

            for i in range(dir_level+1):                                    #   compose full directory name from list current_short_path[]
                dir_path_branch_full_2= os.path.join(dir_path_branch_full_2, current_short_path[i])
            #   print(f' Dir to be created : {dir_path_branch_full_2}')
            dir_create_if_not_exists(dir_path_branch_full_2)                #   create file if not exist


        if obj1 == 'file':
            dir_path_branch_full_2 = dir_path_branch_full_1
            for i in range(dir_level):                                              #   compose full directory name from list current_short_path[]
                dir_path_branch_full_2= os.path.join(dir_path_branch_full_2, current_short_path[i])
            file_path_branch_full_2= os.path.join(dir_path_branch_full_2, name1)    #   compose full file name
            #   print(f' File to be created : {file_path_branch_full_2}')
            file_create_if_not_exists(file_path_branch_full_2, '111111 \n ')        #   create file if not exist



