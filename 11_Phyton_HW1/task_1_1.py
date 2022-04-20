# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах.
# Условие задачи
# Техническое задание:
#
# duration - целое число: время в секундах. Вы можете вводить duration с клавиатуры или сразу занести в код.
# Формат вывода результата:
#
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры/Тесты:
#
# duration = 53: 53 сек
# duration = 153: 2 мин 33 сек
# duration = 4153: 1 час 9 мин 13 сек
# duration = 400153: 4 дн 15 час 9 мин 13 сек
#

sec_in_day = 86400
sec_in_hour = 3600
sec_in_minute =60

print('   The program calculated days, hours, minutes and seconds ')

while True:
    try:
        duration = int(input( ' please enter duration in seconds :  '))
        break
    except ValueError:
        pass

duration = int(duration)
num_days = duration // sec_in_day
num_hours = ( duration % sec_in_day ) // sec_in_hour
num_minutes = ( duration % sec_in_hour ) // sec_in_minute
num_seconds = duration % sec_in_minute

result = ' период соответствует : '
if num_days :
    result = result + str(num_days)+' дн '
if num_hours:
    result = result + str(num_hours) + ' час '
if num_minutes:
    result = result + str(num_minutes) + ' мин '
if num_seconds:
    result = result + str(num_seconds) + ' сек '

print(result)