# 1. Написать функцию 'email_parse(<email_address>)',
# которая при помощи регулярного выражения извлекает
# имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.

# Техническое задание:
#
# Функция:
# принимает параметр: строка email, при необходимости и другие параметры
# извлекает имя пользователя - то, что до знака @ и домен - то, что после знака @
# возвращает словарь вида {'username': <имя_пользователя>, 'domain': <домен>}
# Если адрес не валиден, выбросить исключение 'ValueError'. Можно с сообщением вида «wrong email: <email_address>»
# Шаблон имени пользователя: латинские буквы, цифры и символы: '._+-
# Шаблон домена: латинские буквы, цифры и символы .-
# В домене обязательно должна быть хотя бы одна точка
# Не использовать методы строки для извлечения информации из email - только регулярные выражения
# email полностью парсится за «один проход». Используйте группы.
# Проверьте работоспособность функции на прилагаемых тестовых email (файл task_8_1_test_email.txt). Попытайтесь добиться, чтобы для всех примеров ваша программа работала правильно. Допускаются 2-3 рассогласования.
# Чтобы проверить работоспособность функции на разных данных, вам придется «ловить» исключение в основной программе и выводить сообщение.
# Примеры/Тесты:
#
#
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru


import re

RE_PATERN = re.compile(r"""
        (^|\A|\s)
        (?P<name>[a-z\d._+-]+'?[\w\d._+-]+)
        @
        (?P<domname>[a-z._-]+
        \.
        [\w._-]{2,})
        """, re.VERBOSE)


#string = input('Please enter string from mail : ')

'''
text1
string = """# >>> email_parse('someone@geekbrains.ru')
 {'username': 'someone', 'domain': 'geekbrains.ru'}
 >>> email_parse('someone@geekbrainsru')
 Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
   ...
     raise ValueError(msg)
 ValueError: wrong email: someone@geekbrainsru"""
'''

string = """ text2
user0_name@domenname.ru           {'username': 'user0_name', 'domain': 'domenname.ru'}
user1'name@domenname.ru           {'username': "user1'name", 'domain': 'domenname.ru'}
user2.name@domenname.ru           {'username': 'user2.name', 'domain': 'domenname.ru'}
user3+name@domenname.ru           {'username': 'user3+name', 'domain': 'domenname.ru'}
user4-name@domenname.ru           {'username': 'user4-name', 'domain': 'domenname.ru'}
user5=name@domenname.ru           Error
user6*name@domenname.ru           Error
user7&name@domenname.ru           Error
user8^name@domenname.ru           Error
user9%name@domenname.ru           Error
user10$name@domenname.ru          Error
user11#name@domenname.ru          Error
user12_name@domenna.me.ru         {'username': 'user12_name', 'domain': 'domenna.me.ru'}
user13_name@domennameru           Error
user14_name@domen-name.ru         {'username': 'user14_name', 'domain': 'domen-name.ru'}
user16_name@domen+name.ru         Error
user17_name@domen=name.ru         Error
user18_name@domen)name.ru         Error
user19_name@domen*name.ru         Error
user20_name@domen/name.ru         Error
user21_name@domen&name.ru         Error
user22_name@domen%name.ru         Error
Юзер23_name@domenname.ru          Error
user24_name@доменname.ru          Error
user25_name@domen,name.ru         Error
user26_name@domen<name.ru         Error
user27>name@domenname.ru          Error"""




string=string.split('\n')


for string1 in string:
    try:
        parse_result3 = RE_PATERN.search(string1)
        result = parse_result3.groupdict()
    except AttributeError as e:
        result = e
    finally:
        print(f"\nString: {string1}")
        print(f"ГРУППЫ словарем: {result} ")
