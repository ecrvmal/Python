# 4. Обработка списка чисел.
# Техническое задание
#
# Создать список, содержащий цены на товары (10 – 20 товаров), например: [57.8, 46.51, 97, ...].
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). Обратите внимание на изменение формата вывода.
# Вывести на экран цены(как числа), отсортированные по возрастанию, новый список для этого не создавать (показать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию. Показать, что это другой список, другой объект,
# Вывести цены пяти самых дорогих товаров.
# Список может содержать произвольное кол-во элементов.
# Часть цены в рублях оставляем без изменения. Нули добавляем только к копейкам.
# Считаем, что например 57.8 это 57 рублей и 80 копеек, а 8.04 это 8 рублей и 4 копейки.
# Обратите внимание на требование создавать или не создавать новый список. Не путайте создание нового списка и присваивание его некоторой переменной.
# Регулярные выражения не используем. Учимся парсить самостоятельно.
# Формат вывода результата:
#
#
#    Исходный список:
# [57.8, 46.40, 97, 12.3, 67.54, 8.07, 982.12]
# 57 руб 80 коп, 46 руб 40 коп, 97 руб 00 коп, 12 руб 30 коп, 67 руб 54 коп, 8 руб 07 коп, 982 руб 12 коп,
# Доказательство операции in place:
#     id перед сортировкой хххххххх
#     id после сортировки хххххххх
# [8.07, 12.3, 46.4, 57.8, 67.54, 97, 982.12]
# 5 самых дорогих товаров:
#     982.12
#     97
#     67.54
#     57.8
#     46.4

num_of_expensive =5

def print_prises(lst):
    string3 = ''
    for price in lst:
        string3 += f' {int(price)} руб {int(price*100 - int(price)*100):02d} коп ,'
    print(string3[:-2])


string3 = ''
prices =[57.8, 46.51, 97, 56.8, 99.99, 1.3, 3.62, 4.12 ]

print ( '\n  Input data : ')
print(prices)

print ( '\n  initial list : ')
print_prises(prices)
list_id_old=id(prices)

print ( '\n  List sorted by increase : ')
prices.sort()
print_prises(prices)
print ('\n  Доказательство операции in place:')
print(f' list id before sort :  {list_id_old} ')
print(f' list id after sort  :  {id(prices)} ')

print ( '\n  New list sorted by decrease : ')
new_prices = sorted(prices, reverse=True)
print_prises(new_prices)
print(f' list id = {id(new_prices)} ')


print('\n 5 the  most expensve goods : ')
for pr in new_prices[:num_of_expensive]:
    print(f' {pr:5.2f}')
