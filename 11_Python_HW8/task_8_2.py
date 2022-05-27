# 2. [Задача со звездочкой]: усложненный вариант задания
# 2.1. Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# Техническое задание:
#
# Лог файл: https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs
# Функция парсинга строки лог-файла:
# Принимает параметр: строка для пасинга, при необходимости и другие параметры
# возвращает кортеж из 6 элементов вида: ('<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>)'
# Вы можете не обращать внимание на IPv6 или явно учесть их в регулярном выражении, это будет очень хорошо.
# Проверьте работоспособность функции на нескольких строках лог файла.
# Распарсите весь файл и сформируйте список всех IP лог файла, без повторений. Выведите в консоль его длину.
# Примеры/Тесты:
#
#
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
#
# Усложнение:
#
# Ваша функция должна корректно обрабатывать как IPv4, так и IPv6 - найдите их в лог-файле.
# Посмотрите спецификацию IPv6. Что такое шестнадцатеричное число и какие буквы/цифры оно может включать. Сколько их может быть в IPv6.
# Совсем хорошо, если вы обработаете cокращенные адреса IPv6, которые тоже в есть в лог файле.
# Ваш шаблон должен пропускать только то, что нужно, не используйте «избыточно широкие» шаблоны.

import re
import requests
import urllib


RE_PATERN = re.compile(r"""
    (^|\A|\s)
    (?P<rem_addr>((\d{1,3})(\.\d{1,3}){3})|
    (([0-9]|[a-f]){,4})(:([0-9]|[a-f]){,4}){6,7})
    \s-\s-\s
    (?P<request_datetime>\[\d{2}\/[A-Z][a-z]{2}\/\d{4}(:\d{2}){3}\s\+0000\])\s\"
    (?P<request_type>[A-Z]+)\s
    (?P<requested_resource>/downloads/product_\d\sHTTP/1.1)\"\s
    (?P<response_code>\d+)\s
    (?P<response_size>\d+)
""", re.VERBOSE)

#string = input('Please enter string from mail : ')

url_addr = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs"

response = requests.get(url_addr)
print(response)
#print(type(response)) # <class 'requests.models.Response'>
#print(dir(response))

ip_list = set()


with urllib.request.urlopen(url_addr) as content:
    print(f'url opened')
    for _ in content:
        line_content = str(content.readline().decode('utf-8'))
        print("\n",line_content)
        try:
            parse_res = RE_PATERN.search(line_content)
            result = parse_res.groupdict()
        except AttributeError as e:
            result = e
        finally:
            print(f"ГРУППЫ словарем: {result} ")
        ip_address=result['rem_addr']
        #print(result)
        #print(type(result))
        print (f'ip_address = ',ip_address)

        #print  ('ip_address= ', ip_address)
        if ip_address not in ip_list :
            ip_list.add(ip_address)
            print (f'IP added {ip_address}')
print(f'\n\nLength of IP list, including IPv6  is : {len(ip_list)}')

