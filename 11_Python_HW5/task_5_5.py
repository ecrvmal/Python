# 5. Задан список чисел. Определить элементы списка,
# не имеющие повторений.
# Сформировать из этих элементов список с
# сохранением порядка их следования в исходном списке
#
# Техническое задание
#
# Здесь нет условия создавать итератор/генератор или comprehensions.
# Сохранение исходного порядка в результирующем списке обязательно.
# Не используйте Counter из модуля collections или аналогичные.
# Примеры/Тесты:
#
#
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = []
if not src[0] in src[1:]:               # check 1-st element
    result.append(src[0])
for i in range(len(src)-1):             # check i element
    if not src[i] in src[:i] and not src[i] in src[i+1:]:
        result.append(src[i])
if not src[len(src)-1] in src[:-2]:     # check last element
    result.append(src[len(src)-1])

print(f' src    : {src}')               # print initial list
print(f' result : {result}')           # print result list
