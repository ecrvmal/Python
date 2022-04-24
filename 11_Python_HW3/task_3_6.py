# 6. Реализовать функцию get_jokes(), возвращающую n шуток,
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
# 6         Техническое задание
#
#         Добавьте в функцию еще один аргумент, разрешающий или запрещающий повторы слов в шутках:
#         каждое слово можно использовать только в одной шутке.
#         Тогда этот параметр логично сделать типом boolean.
#         Функция должна вернуть список строк-шуток сколько потребовали или
#         сколько получилось из условия уникальности.
#         Проверьте работу функции для разного количества шуток.
#         Убедитесь в том, что каждое слово встречается только один раз.

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]



def get_jokes(n, list1, list2, list3, single_use=False ):
    list1a = list1[::1]             # make a local copy of list1
    list2a = list2[::1]             # make a local copy of list2
    list3a = list3[::1]             # make a local copy of list3
    diagnostic = ''
    result = []

    if not single_use:
        for i in range(n):          # cycle  for n - Jokes
            string1 = f'{random.choice(list1)} {random.choice(list2)} {random.choice(list3)}'  # create string of random words
            result.append(string1)
        return result

    else:

        for i in range(n):                                      # cycle  for n - Jokes
            if list1a:                                          # Check if list isn't empty
                word1 = random.choice(list1a)                # choose random word1 and take-out word from list
                list1a.remove(word1)
            else:
                string2 = f'*** Diags: words in "nouns" list  ended'         # if list is empty : create diagnostic string and Append diagn. to result
                result.append(string2)                          #   and Append diagn. string  to result
                return result                                   # and return result with diagnostic
            if list2a:
                word2 = random.choice(list2a)                # choose random word1 and take-out word from list
                list2a.remove(word2)
            else:
                string2 = f'*** Diags: words in "adverbs" list  ended'
                result.append(string2)
                return result
            if list3a:
                word3 = random.choice(list3a)               # choose random word1 and take-out word from list
                list3a.remove(word3)

            else:
                string2 = f'*** Diags: words in "adjectives" list  ended'    # diagnostic string
                result.append(string2)                      # create of  jokes-string with diagnistic
                return result                               # return of  jokes-string with diagnistic

            string1 = f'{word1} {word2} {word3}'            # create string of random words
            result.append(string1)                          # append string to jokes-string

        #  print(result)                                    # print for debug-purposes
        return result                                       # return of  jokes-string

# def get_word(list_name):
#     nonlocal list_name
#     word1 = random.choice(list_name)
#     list_name.remove(word1)
#     return word1

# def diagnostic(list_name1):
#     nonlocal result
#     string2 = f'words in adjectives {list_name1}  ended'  # diagnostic string
#     result.append(string2)
#     return result

def prnt_jokes (jokes_list):
    for joke in jokes_list:
        print (f'  {joke} ')
    return




# main()
# call sub-function with positioned args
print('\n ***  call sub-function with "positioned"  args  *** \n')
prnt_jokes(get_jokes(10, nouns, adverbs, adjectives))

# call sub-function with named args:
print('\n *** call sub-function with "named"  args  *** \n')
prnt_jokes(get_jokes(list3=adjectives, list2=adverbs,  list1=nouns, n=20))

# call sub-function with named args and "Word_Single_Use"):
print('\n ***   call sub-function with "named"  args and "Word_Single_Use"   *** \n')
prnt_jokes(get_jokes(list3=adjectives, list2=adverbs,  list1=nouns, n=20, single_use=True))