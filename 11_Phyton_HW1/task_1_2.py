# 2. Для кубов нечётных чисел от 1 до 1000. Вычислить сумму чисел, сумма цифр кубов которых делится нацело на 7.
# Условие задачи
# Техническое задание:
#
# Для всех нечетных чисел диапазона [1, 1000]
# вычислить их куб
# вычислить сумму цифр куба
# если сумма цифр куба делится нацело на 7, то добавить в накопительную сумму исходное число.
# При решении задачи использовать только арифметические операции и цикл while.
# Не используем списки, функцию range, преобразование числа в строку/список.
# Ваш алгоритм должен корректно работать для всех чисел интервала от 1 до 1000,
# но и легко изменяться для другого диапазона чисел, например от 1 до 10000000.
# Формат вывода результата:
# Вывод на экран формить в виде: число ^3 = куб_числа; [сумма цифр куба] накопительная_сумма
# Например:
#
# 19 ^3 = 6859 [ 28 ] накоп. сумма: 19
# 31 ^3 = 29791 [ 28 ] накоп. сумма: 50
# 43 ^3 = 79507 [ 28 ] накоп. сумма: 93
# 49 ^3 = 117649 [ 28 ] накоп. сумма: 142
# 53 ^3 = 148877 [ 35 ] накоп. сумма: 195
# 55 ^3 = 166375 [ 28 ] накоп. сумма: 250
# ...
# 967 ^3 = 904231063 [ 28 ] накоп. сумма: 43106
# Примечание:
#
# число 19, 19 ^ 3 = 6859, сумма чисел 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Поэтому 19 включаем в вывод.
# Сумма считается для самих чисел 19, 31, 43 и т.п. Не для кубов.

max_number = 1000
i = 1
sum_result=0

while i <= max_number :
    sum_of_digits = 0
    cube = i ** 3
    digit = cube
    while True:
        element =  digit % 10        # take last digit
        sum_of_digits += element     # add the element to  summ
        if element == digit:         # if this is last element in digit then exit
            break
        else:
            digit = digit // 10        # shift digits to 1 place

    if sum_of_digits % 7 == 0:
        sum_result += i
        print (' i = ',i, '   cube = ',cube, '[' , sum_of_digits,']', 'Summ = ', sum_result  )
    i += 1

print('\n  Task result :  ' ,  sum_result )