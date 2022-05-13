# 4. Задан список чисел.
# Необходимо создать список, содержащий те его элементы,
# значения которых больше предыдущего.
#
# Техническое задание
#
# Здесь нет условия создавать итератор/генератор. Можно использовать comprehensions.
# Формально первый элемент сравнить не с чем.
# Решите сами, что с ним делать: включать в новый список или нет.
# Можете сравнить его с последним элементом.
# Примеры/Тесты:
#
#
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]




# main()
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print('     solution with FOR cycle  : ')
result = []
if src[0] > src[-1]:
    result.append(src[0])
for i in range(1, len(src)):
    if src[i] > src[i-1]:
        result.append(src[i])

print(f' src    : {src}')
print(f' result : {result}')

print('\n \n    solution with comprehension  : ')

result1 = [a for a, b in zip(src[1:], src) if a > b ]
print(f' src    : {src}')
print(f' result1 : {result1}')




#result= [el  for el in src if el > ]