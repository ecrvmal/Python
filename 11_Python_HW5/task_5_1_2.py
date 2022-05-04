# 1. Написать генератор нечётных чисел от 1 до n (включительно), без использования ключевого слова yield, полностью истощить генератор.
# Формат вывода результата:
#
# Программа явно должна закончиться на StopIteration
# Техническое задание
#
# n - любое положительное число.
# Создание генератора сделайте внутри функции iterator_without_yield(n), примающей аргументом n любое положительное число и возвращающей генератор.
# Не путайте истощение генератора и печать его значений. Выполнение программы должно закончиться на исключении StopIteration. Истощение генератора - любым удобным для вас способом.
#
# Усложнение [одна звездочка]:
# нужен генератор нечётных чисел от 1 до n (включительно),
# для чисел, квадрат которых меньше 200. Все остальное как в основном задании.
#
# Примеры/Тесты:
#
#
# gen1 = iterator_without_yield(11)
# next(gen1)
# 1
# next(gen1)
# 3
# next(gen1)
# 5
# next(gen1)
# 7
# next(gen1)
# 9
# next(gen1)
# 11
# next(gen1)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration


def iterator_without_yield(n):
    return (num for num in range(1, n + 1, 2) if num ** 2 < 200)


# main()
value = int(input('Please enter value to generate GEN: '))
gen1 = iterator_without_yield(value)
while True:
    print(f'next(gen1) =  {next(gen1)}')
