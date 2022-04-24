# 2. [Задача со звездочкой]: усложненный вариант задания 1.
# Написать функцию num_translate_adv, которая корректно обработает числительные, начинающиеся с заглавной буквы. Если перевод сделать невозможно, вернуть объект None.
# Условие задачи
# Техническое задание
#
# Функция возвращает строку перевод. Или возвращает None, если перевести невозможно.
# Считаем, что только первая буква может быть заглавной.
# Обратите внимание, что функция возвращает перевод в том же регистре как и приняла.
# Выполнить вызов функции для нескольких слов и вывести на экран результаты.
# Примеры/Тесты:
#
#
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"



def num_translate_adv(word1):
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
    title_letter = True if word1.istitle() else False
    for key in dict1.keys():
        if word1.lower() == key and title_letter:
            return dict1[key].capitalize()
        elif word1.lower() == key and not title_letter:
            return dict1[key]
        else:
            pass
    return


print(f'   PROGRAMM - DIGIT  TRANSLATOR ')
while True:
    word = input('please enter digit as a word , or q for exit : ')
    if word.lower() =='q':
        print(f' Programm ended ')
        break
    translation = num_translate_adv(word)
    if not translation:
        pass
    else:
        print(translation)

