# 2. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield. Полностью истощить генератор.
# Техническое задание
#
# Все пункты ТЗ задания 1 остаются в силе.
# Отличие от задания 1 - только в использовании yield.
# Усложнение [одна звездочка]:
# С ключевым словом yield - как в задании 1: генератор нечётных чисел от 1 до n (включительно),
# для чисел, квадрат которых меньше 200.
#
# Усложнение [две звездочки]:
# С ключевым словом yield:
# Вычислять и возвращать само число и накопительную сумму этого и предыдущих чисел. Например:
#
#
# gen1 = iterator_with_yield(14)
# next(gen1)
# (1, 1)
# next(gen1)
# (3, 4)
# next(gen1)
# (5, 9)
# next(gen1)
# (7, 16)
# next(gen1)
# (9, 25)
# next(gen1)
# (11, 36)
# next(gen1)
# (13, 49)
# next(gen1)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration


def iterator_with_yield(n):
    for num in range(1, n + 1, 2 ):
        if num ** 2 < 200:
            yield num


# main()
value = int(input('Please enter value to generate GEN: '))
gen1 = iterator_with_yield(value)
while True:
    print(next(gen1))
