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
#
# 2. [Задача со звездочкой]: усложненный вариант задания 1.
# Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Спамер — это клиент, отправивший больше всех запросов.
# Формат вывода результата:
#
# Вывести IP спамера и количество запросов от него.
# Техническое задание
#
# Код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# У нас изначально нет никакой информации о максимальном количестве запросов. Его надо определить из лог-файла.
# Не используйте сторонние модули для подсчетов, типа «count» - они вам не нужны.
# Не используйте затратные операций типа сортировки и поисков. Они здесь абсолютно избыточны.
# Для примера представьте, что более половина лог-файла - это запросы от спамера. Оцените эффективность вашего алгоритма в таком случае.


file1 = open(file="./task_6_1.dat", mode="rt", encoding="utf-8")

result_lst = []
spamer_dict = {}

while True:
    string1 = file1.readline()
    if string1 == '':
        break
    string1a = string1[:string1.find('-')-1]    #   93.180.71.3
    string2 = string1.split('"')[1]            #   GET /downloads/product_1 HTTP/1.1
    string2a = string2.split('/')[0][:-1]       #   GET
    string2b = string2.split(' ')[1][1:]        #   downloads/product_1

    #result_tup = (string1a,string2a,string2b)
    #print(result_tup)                          # used for debugging
    #result_lst.append(result_tup)

    if string1a in spamer_dict:
        spamer_dict[string1a] += 1
    else:
        spamer_dict[string1a] = 1

file1.close()

# for ip_addr, num_calls in spamer_dict.items():      # used for debugging
#     print(ip_addr, ' : ', num_calls)                # used for debugging


ip_max_calls = max(spamer_dict, key=spamer_dict.get)
print('\n Spammer detected, \n')
print(f' Spammer works from  IP :  {ip_max_calls} , num of requests : {spamer_dict[ip_max_calls]}')
