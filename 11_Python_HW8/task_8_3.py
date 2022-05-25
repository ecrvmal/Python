# 3. Написать декоратор для логирования(вывод в консоль) типов позиционных аргументов функции:

# Техническое задание:
#
# Если аргументов несколько - выводить данные о каждом через запятую.
# Все выводы должны быть внутри функции-обертки/задекорированной функции
# После того как вы «обернули»/«задекорировали» функцию убедитесь что и аргументы, и возвращаемое значение остались как у исходной функции.
# Т.е. вызов задекорированной функции ничем не отличается от вызова исходной функции, результат возвращается такой же, но добавляется печать в консоль.
# Примеры/Тесты:
#
#
# def type_logger...
#     ...
#
# @type_logger
# def render_input(*args):
#    return 1
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# Call for: calc_cube
# 5: <class 'int'>
# Rezult: 125  type: <class 'int'>
#
# >>> render_input(1, a = 2, b = True, c = "q")
# Call for: render_input
# 1: <class 'int'>
# 'a' = 2: <class 'int'>, 'b' = True: <class 'bool'>, 'c' = q: <class 'str'>
# Rezult: 1  type: <class 'int'>
#
# Усложнение:
#
# вывести тип возвращаемого значения функции
# решить задачу для именованных аргументов
# вывести имя функции

def create_wrapper(func):
    def wrapper(*args, **kwargs):
        print(f'wrapper: Working module name:  {func.__name__} ')
        print('wrapper: args : ', end='')
        for el in args: print(f' {el}', end='')

        print('\n wrapper: kwargs : ' , end='')
        for el in kwargs: print(f' {el} : {kwargs[el] }; ', end='')
        print('\n')
        rezult = func(*args, **kwargs)
        return rezult
    return wrapper

def calc_cube(x, y=0, z=0):
    return x ** 3 - y - z

def render_input(*args):
    return 1

# Run the function without wrapper :
print (f'\nmain: Run calc cube without wrapper ')

print(f'main: result: {calc_cube(3, z=2)}')
print(f'main: Type of result: {type(calc_cube(3, z=2))}')

# Now run the function with wrapper :
calc_cube = create_wrapper(calc_cube)              #   function can be wrapped with the same name
print (f'\nmain: now run calc cube with wrapper ')

print (f'\nmain: {calc_cube(3, z=2)}')          # wrapper now  prints args to console
print (type(calc_cube(3, z=2)))                 # wrapper now  prints args to console and type(rezult)

# Run the function render_input  without wrapper :
print (f'\nmain: Run render_input cube without wrapper ')
print(f'\nmain: {render_input(1, True, "this is string", 4.12 )}')

# Now run the function with wrapper :
print (f'\nmain: now run render_input with wrapper ')
render_input = create_wrapper(render_input)                                     #   function can be wrapped with the same name
render_input(1, True, "this is string", 4.12 )
print (f'main: {render_input(1, True, "this is string", 4.12 )}')                           # wrapper now  prints args to console
print (f'main: Type of result: {type(render_input(1, True, "this is string", 4.12 ))}')     # wrapper now  prints args to console and type(rezult)