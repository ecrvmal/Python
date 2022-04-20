# 1. Выяснить тип результата следующих выражений:
# 15 * 3
# 15 / 3
# 15 // 2
# 15 ** 2
# Техническое задание:
# Вывести на экран тип выражения и отдельно проверить является ли полученный тип целым числом.


print (f' 15 * 3 : type : {type(15 * 3)}')
print (f' is INT : {isinstance(15*3 , int) } \n')

print (f' 15 / 3 : type : {type(15 / 3)}')
print (f' is INT : {isinstance(15 / 3 , int) } \n')

print (f' 15 // 2 : type : {type(15 // 2)}')
print (f' is INT : {isinstance(15 //2  , int) } \n')

print (f' 15 ** 2 : type : {type(15 ** 2 )}')
print (f' is INT : {isinstance(15 ** 2  , int) } \n')
