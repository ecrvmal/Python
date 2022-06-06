# 3. Создайте собственный класс-исключение, используемый для проверки содержимого списка на наличие только чисел.
# Техническое задание:
#
# Собственный Класс-исключение используется только для «подмены» исключения.
# Вы можете создать в нем конструктор, если хотите наполнить его данными.
# Данные запрашиваются у пользователя по одному элементу.
#
# Длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
# введя, например, команду «stop» или пустую строку.
# Список заполняется только числами. Для простоты ввода - целыми.
#
# При вводе не числа выбрасывается исключение. Оно корректно обрабатывается и ошибочные данные в список не заносятся.
# Отобразить диагностическое сообщение о неправильном вводе.
# Примечание:
#
# Вы можете написать функцию для проверки корректности введенных пользователем данных,
# тогда исключение должно выбрасываться в ней,
# такой вариант предпочтительнее. Но можете все делать в основной программе,
# тогда вам могут понадобятся вложенные блоки 'try except', а могут и не потребоваться.

class NotDigitException(ValueError):
    def __init__(self, info):
        self.info = ''


def convert_to_int(value):
    try:
        int_value = int(value)
        return int_value
    except ValueError:
        raise NotDigitException(f"the {value} is not an integer")


print(' Program checks if value is int  \n')
result_list = []
while True:
    a = input("Please input Value or 'enter' for exit :  " )
    try:
        if a == '' : break
        a = convert_to_int(a)
        result_list.append(a)
    except NotDigitException as err:
        print(err)

print (f" Result list = {result_list}")
print('\n Program ended ')

# Console_Output:
#  Program checks if value is int
#
# Please input Value or 'enter' for exit :  1
# Please input Value or 'enter' for exit :  2
# Please input Value or 'enter' for exit :  3
# Please input Value or 'enter' for exit :  4
# Please input Value or 'enter' for exit :  f
# the f is not an integer
# Please input Value or 'enter' for exit :  g
# the g is not an integer
# Please input Value or 'enter' for exit :  6
# Please input Value or 'enter' for exit :  7
# Please input Value or 'enter' for exit :  8
# Please input Value or 'enter' for exit :
# the   is not an integer
# Please input Value or 'enter' for exit :
#  Result list = [1, 2, 3, 4, 6, 7, 8]
#
#  Program ended
#
# Process finished with exit code 0

