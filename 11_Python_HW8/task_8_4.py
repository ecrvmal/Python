# 4. [Задача с двумя звездочками]: усложненный вариант задания 3.
# Написать декоратор с аргументом-функцией (callback),
# позволяющий валидировать входные значения функции и выбрасывать исключение ValueError, если что-то не так
#
# Техническое задание:
#
# Посмотрите как реализуется декоратор с параметром в методичке - еще один уровень вложенности
# Не используйте поиск решения в интернете вообще (от слова совсем) - попытайтесь разобраться по методичке что происходит.
# Переданная функция вычисляется от параметров, если True, то возвращаем результат, если False - выкидываем исключение.
# Сможете ли вы замаскировать работу декоратора? Это тоже рассмаотрено в методичке.
# Примеры/Тесты:
#
#
# def val_checker...
#     ...
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5

def val_checker(func1):
    def create_wrapper(func):
        def wrapper(*args):
            if func1(*args):
                result = func(*args)
                pass
                return result
            else:
                raise ValueError
        return wrapper
    return create_wrapper


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3



try:
#    a =  calc_cube(-5)                     # Use this for Raise exception
    a = calc_cube(5)                        # Use this for normal process completion
    print(a)
except ValueError:
    print('negative value x ')