# 5. Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх заданных списков.
# Условие задачи
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
# Техническое задание
#
# Функция должна вернуть список строк-шуток.
# Функция принимает 4 параметра: количество шуток и 3 списка со словами.
# В списках nouns, adverbs, adjectives не обязательно одинакое количество элементов. Они могут быть произвольной длины.
# Проверьте работу функции для количества шуток больше, чем длины списков слов и меньше.
# Сделайте вызов функции как с позиционными аргументами, так и с именованными.
# Менять исходные списки nouns, adverbs, adjectives нельзя. Это «side effects»
# Документируйте код функции.
# Примеры/Тесты:
#
#
# >>> get_jokes(3, nouns, adverbs, adjectives)
# ['автомобиль ночью мягкий', 'лес сегодня утопичный', 'дом вчера зеленый']
# >>> get_jokes(5, nouns, adverbs, adjectives)
# ['автомобиль вчера зеленый',
#  'дом ночью мягкий',
#  'огонь ночью утопичный',
#  'дом позавчера зеленый',
#  'город вчера утопичный']
# >>>

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n, list1, list2, list3 ):
    result = []
    # print(f'Subprogram returns  {n}  JOKES :')
    for i in range(n):                              # cycle  for n - Jokes
        string1 = f'{random.choice(list1)} {random.choice(list2)} {random.choice(list3)}'  # create string of random words
        result.append(string1)                                                             # append string to jokes-string
    #  print(result)                                                                       # print for debug-purposes
    return result                                                                          # return of  jokes-string

# main()
# call sub-function with positioned args
print('\n call sub-function with "positioned"  args')
print (get_jokes(5, nouns, adverbs, adjectives))

# call sub-function with named args:
print('\n call sub-function with "named"  args')
print (get_jokes(list3=adjectives, list2=adverbs,  list1=nouns, n=7))

