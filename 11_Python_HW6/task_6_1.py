# 1. Распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# Техническое задание
#
# Не использовать библиотеки для парсинга. Только работа со строками.
# Создать список кортежей вида: '(<remote_addr>, <request_type>, <requested_resource>)'. Именно список кортежей.
# Код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# Вывести список на экран.
# Формат вывода результата:
#
#
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'HEAD', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_1'),
#     ...
# ]
#
# Примечание:
#
# Файл логов можно загрузить отсюда:
# https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs


file1 = open(file="./task_6_1.dat", mode="rt", encoding="utf-8")

result_lst = []

while True:
    string1 = file1.readline()
    if string1 == '':
        break
    string1a = string1[:string1.find('-')-1]    #   93.180.71.3
    string2 = string1.split('"')[1]            #   GET /downloads/product_1 HTTP/1.1
    string2a = string2.split('/')[0][:-1]       #   GET
    string2b = string2.split(' ')[1][1:]        #   downloads/product_1

    result_tup = (string1a,string2a,string2b)
    #print(result_tup)                          # used for debugging
    result_lst.append(result_tup)

file1.close()

for res_line in result_lst:
    print(res_line)