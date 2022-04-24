# 1. Написать функцию num_translate, переводящую числительные от 0 до 10 c английского на русский язык.
# Условие задачи
# Техническое задание
#
# Функция num_translate возвращает строку перевод. Или возвращает None, если перевести невозможно. Обратите внимание, что возвращается None как объект, а не как строка "None". Не путайте печать значения (print) и его возврат из функции (return).
# Функция принимает параметр - строку слово для перевода, и другие параметры, если нужно - по вашему усмотрению. В примере специально они не указаны.
# Здесь нет требований на регистр входного слова. Возвращается результат в нижнем регистре.
# Выполнить вызов функции для нескольких слов и вывести на экран результаты.
# Примеры/Тесты:
#
#
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"



def num_translate(word1):
    dict1 = {
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять"
    }
    for key in dict1.keys():
        if word1.lower() == key:
            return dict1[key]
    return

print(f'   PROGRAMM - DIGIT  TRANSLATOR ')
while True:
    word = input('please enter digit as a word , or q for exit : ')
    if word.lower() =='q':
        print(f' Programm ended ')
        break
    translation = num_translate(word)
    if not translation:
        pass
    else:
        print(translation)


