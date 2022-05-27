# 3. Создать структуру файлов и папок, как написано в задании 2
# (при помощи скрипта или «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates:
#
# |--my_project
# ...
# |--templates
# |   |--mainapp
# |   |  |--base.html
# |   |  |--index.html
# |   |--authapp
# |   |  |--base.html
# |   |  |--index.html
#
# Техническое задание
#
# Шаблон - это папка templates в исходной структуре папок.
# Ее уровень в структуре папок может быть любым. В папках mainapp, authapp и аналогичных могут быть и другие файлы,
# с другими раширениями, кроме тех что приведенны в примере.
# Папку templates надо создать внутри исходной директории, в примере - внутри my_project
# Исходные файлы и папки необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён).
# Предусмотреть возможные исключительные ситуации;
# Примечание:
#
# это вполне реальная задача, которая решена, например, во фреймворке django.

import os, shutil


def dir_create_if_not_exists(dir_path_full):
    if not os.path.exists(dir_path_full) or not os.path.isdir(dir_path_full):
        os.mkdir(dir_path_full)
        print(f' Folder created         : {dir_path_full} ')
    else:
        print(f' Folder already exists  : {dir_path_full} ')


dir_path_full = os.path.join(os.getcwd(), 'task_7_3' )
# print (f'dir_path_full {dir_path_full}')
template_dir = os.path.join(dir_path_full, "my_project", "templates")
# print (f'template_dir {template_dir}')
dir_create_if_not_exists(template_dir)


for root, dirs, files in os.walk(dir_path_full):
    # print(f'root : {root} , dirs : {dirs} , files {files}')
    if root.endswith("\\templates"):
        if root != os.path.join(dir_path_full, "my_project", "templates"):
            # copy all dirs
            for dir_el in dirs:
                path_src = os.path.join(root, dir_el)
                path_dst = os.path.join(template_dir, dir_el)
                try:
                    shutil.copytree(path_src,path_dst)
                    print (f' folder has been copyed : {path_dst}')
                except FileExistsError as exception_item:
                    print (f' can not copy file, folder already exists : {exception_item} ')
            # copy all files
            for file_el in files:
                path_src = os.path.join(root, file_el)
                path_dst = os.path.join(template_dir, file_el)
                try:
                    shutil.copytree(path_src, path_dst)
                    print(f' folder has been copyed : {path_dst}')
                except FileExistsError as exception_item:
                    print(f' can not copy file, File already exists : {exception_item} ')

print(f"\n  i've moved all i could , bye - bye ")