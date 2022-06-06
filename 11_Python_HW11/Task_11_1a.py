# 1. Реализовать класс «Дата».
# Техническое задание:
#
# Конструктор принимает дату (параметр) в виде строки формата «день-месяц-год».
# Создать методы:
# Первый с декоратором @classmethod.
# Извлекает число, месяц, год из строки «день-месяц-год», преобразовывает их к типу 'int'.
# Возвращает три числа, если не получилось - выкидывает исключение (тип исключения на ваш выбор)
#
# Второй с декоратором @staticmethod.
# Проводит валидацию этих трех чисел, например, месяц — от 1 до 12, дней в месяце не более 31 - далее на ваш выбор.
# Вы можете использовать пакет datetime для проверки корректности даты.
# Возвращает True или False. Могут ли здесь возникнуть исключения?
# Подумайте какое значимое имя вы дадите этому методу?

# При создании объекта в конструкторе использовать первый метод для извлечения,
# второй для валидации. Только после этого создавать атрибуты.
# Объект «дата» хранится в виде трех чисел отдельно или в контейнере.
# В случае невозможности создать объект контруктор выкидывает исключение DateInitError c внятным диагностическим сообщением.

# Конструктор создает объект только если прошла валидация вторым методом.
# Переопределить метод 'str' для печати числа в виде '2021.12.31'
# Создать несколько экземпляров и распечатать их. Проверить работу на не валидных данных.
# Исключение от конструктора ловить в основном коде программы и подменять выводом диагностического сообщения (любого).
# Примеры/Тесты:
#
#
# >>> lst_date = ["31-12-2021", "32-12-2022", "12-12--2022" ]
# ...
# 2021.12.31
# Дата: 32-12-2022,  результат: Внятное диагностическое сообщение
# Дата: 12-12--2022, результат: Внятное диагностическое сообщение
# >>>
#
# Примечание:
#
# В задании предполагаем что оба метода используются только для конструктора.
# Внутренние проверки вы можете сделать на основе концепций LBYL(проверки и обход «узких» мест) или EAFP(исключения и их обработка).
# Подумайте что логично возвращать методам в случае обоих концепций?


class DateInitError(Exception):
    def __init__(self, txt):
        self.txt = txt


class DataClass():
    def __init__(self, str1):
        string2 = self.data_to_int(str1)
        if DataClass.check_date_value(string2):
            self.date_list = string2
        else:
            raise DateInitError("Incorrect input value")

    @classmethod
    def data_to_int(cls, data_string):
        try:
            int_list = data_string.split('-')
            int_list = [int(a) for a in int_list]
            return int_list
        except ValueError as e:
            raise DateInitError("Incorrect input format")

    @staticmethod
    def check_date_value(list1):
        return len(list1) == 3 and 1 <= list1[0] <= 31 and 1 <= list1[1] <= 12 and 1 <= list1[2]

    def __str__(self):
        return f'{self.date_list[2]}.{self.date_list[1]}.{self.date_list[0]}'


print('\n\tThe program read dates , validate them and print in requested format.')
print('\tIn case input can not be validated, the exception rised. \n')

lst_date = [
    "31-12-2021",
    "32-12-2022",
    "12-12--2022"
        ]

for el in lst_date:
    try:
        dat1 = DataClass(el)
        print(f'for input:  {el} object created : {dat1} ')
        print(f'for input:  {el} printout result : {dat1} \n')
    except DateInitError as e:
        print(f'for input:  {el} result : {e}\n')


# Console Output:
#
# 	The program read dates , validate them and print in requested format.
# 	In case input can not be validated, the exception rised.
#
# for input:  31-12-2021 object created : 2021.12.31
# for input:  31-12-2021 printout result : 2021.12.31
#
# for input:  32-12-2022 result : Incorrect input value
#
# for input:  12-12--2022 result : Incorrect input format
#
#
# Process finished with exit code 0






