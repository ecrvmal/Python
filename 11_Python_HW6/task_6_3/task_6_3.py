# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Загрузить данные из обоих файлов и сформировать словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в текстовый файл. Проверить сохранённые данные.
#
# Техническое задание
#
# Данные файлов синхронизированы построчно: 1-ой строке файла с ФИО соответствует 1-ая строка файла с хобби и т.п.
# При хранении данных используется принцип: одна строка — один пользователь.
# Разделитель между значениями — запятая. Не используем пакеты для парсинга CSV файлов.
# При формировании словаря - хобби следует разделить символом «точка с запятой».
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, то для оставшихся ФИО использовать вместо хобби None.
# Если наоборот — формируем словарь, исходя из количества ФИО и выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Вы можете использовать здесь функции zip и zip_longest, но лучше обойтись без них.
#
# Усложнение:
# Выполните запись результирующего словаря в файл json формата.
# Сделайте так чтобы русские букву читались как обычный текст, без преобразования в коды unicode.

# Примеры/Тесты:
#
# Фрагмент файла с данными о пользователях (task_3_users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Сидоров,Сидор,Сидорович
#
# Фрагмент файла с данными о хобби (task_3_hobby.csv):
# скалолазание,охота
# горные лыжи
# вышивание крестиком, бои без правил
#
# Фрагмент результирующего файла (task_3_rezult.txt):
# {'ИИИ': 'скалолазание;охота', 'ППП': 'горные лыжи', 'ССС': 'вышивание крестиком; бои без правил'}

import json

dict_result = {}
exit_code = 0

with open(file="task_6_3_users.csv", mode="rt", encoding="utf-8") as file_fio:   # the line is for 6 names inpt file
                                                                                # you can comment the line
#with open(file="task_6_3_users2.csv", mode="rt", encoding="utf-8") as file_fio:   # the line is for 2 names inpt file
                                                                                # you can comment the line
    with open(file="task_6_3_hobby.csv", mode="rt", encoding="utf-8") as file_hobby:
        while True:
            str_fio = file_fio.readline()
            if str_fio == '':
                break
            str_fio1 = str_fio.split(',')
            str_fio2 = f'{str_fio1[0][0]}{str_fio1[1][0]}{str_fio1[2][0]}'
            # print(str_fio2)
            str_hobby = file_hobby.readline()
            str_hobby = None if str_hobby == '' else str_hobby.replace(',', ';').strip()
            dict_result[str_fio2]=str_hobby
        if file_hobby.readline() != "":
            exit_code = 1

print(f'\n   Text Result will be stored in file "task_6_3_result.txt" \n {dict_result}')
with open(file="task_6_3_result.txt", mode="wt", encoding="utf-8") as file_out_txt:
    file_out_txt.write(str(dict_result))

# task complication

print(f'\n   JSON Result will be stored in file "task_6_3_result.json" \n {dict_result}')
with open(file="task_6_3_result.json", mode="wt", encoding="utf-8") as file_out_json:
    json.dump(dict_result, file_out_json, ensure_ascii=False, indent=4)

exit(exit_code)
