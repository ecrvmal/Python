# 4. [Задача со звездочкой]: усложненный вариант задания 3.
# Написать функцию thesaurus_adv(), принимающую в качестве аргументов
# строки в формате «Имя Фамилия» и возвращающую словарь,
# в котором ключи — первые буквы фамилий, а значения — словари,
# реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы.
# Условие задачи
# Техническое задание
#
# Количество передаваемых строк в функцию может быть любым. Считаем, что переданы будут только корректные строки.
# Вернуть словарь, с ключами, отсортированными в алфавитном порядке.
# Примеры/Тесты:
# #
# >>> thesaurus_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова",
#            "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Василий Суриков")
# {
#    'А':{
#           'П': ['Петр Алексеев']},
#    'И': {
#           'И': ['Илья Иванов']},
#    'С': {
#           'А': ['Алла Сидорова', 'Анна Савельева'],
#           'В': ['Василий Суриков'],
#           'И': ['Иван Сергеев', 'Инна Серова']}}
#
    # Усложнение:
    # Поменяйте местами фамилию и имя в строках. Т.е. вместо 'Петр Алексеев' в конечный словарь вносить 'Алексеев Петр'
    # Это преобразование не должно потребовать дополнительного прохода по словарю или списку параметров.

list_names = ("Иван Сергеев", "Алла Сидорова", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Василий Суриков")


def thesaurus_adv(workers):
    workers1 =[]
    workers2 = []
    result = {}
    for pers in workers:
        workers1.append(list(pers.split()))                             # convert  ["Иван Сергеев"] to [["Иван"],["Сергеев"]]

    # print(sorted(workers1))                                           # debug print full list of workers

    list_l_surnames = []                                                #
    for surname in workers1:                                            #
        if surname[1][0] in list_l_surnames:                            #
            pass                                                        #
        else:                                                           #
            list_l_surnames.append(surname[1][0])                        # create list of surname - leters

    list_l_surnames.sort()                                              # sort  list of surname - leters
    # print (f'sorted letters {list_l_surnames}')

    for k in list_l_surnames:                                               # cycle by surname-letter
        list_l_names = []
        workers2 = []
        # print (f'k= {k}')
        workers2 = list(filter(lambda x: x[1][0] == k, workers1))           # filter by surname-letter
        # print (f'workers2 = {workers2}')
        for name in workers2:                                               # cycle by name-letter
            if name[0][0] in list_l_names:                                  #
                pass                                                        #
            else:                                                           #
                list_l_names.append(name[0][0])                             # create list of Name - leters
        list_l_names.sort()                                                 # sort list of Name - leters
        #  print(f' list_l_names = {list_l_names}')
        result1 = {}
        for l in list_l_names:
            name_list = []
            name_list1_=[]
            name_list2 = []
            name_list = list(filter(lambda x: x[0][0] == l, workers2))      # Filter by name
            name_list1 = list(map(lambda x:  x[::-1] , name_list))          # convert ['name','surname '] to ['surame','name']
            name_list2 = list(map(lambda x:  ' '.join(x), name_list1))       # convert ['surame','name'] to ['surame _ name']
            result1[l] = name_list2                                         # add to dict { N: ['surame _ name','surame _ name' ]}
            # print(f'result1 = {result1}')
        result[k] = result1                                                 # add to dict {S : { N: ['name_Surname','name_Surname' ]}}
        # print(f'result = {result}')                                       # debug print result
    return result


def print_output (dict0):
    print('function Print Output')
    for letter1, dict1 in dict0.items():                                # Unpack outer dict
        print(f'    {letter1}:  ')                                      # Print S -letter
        for  letter2, dict2 in dict1.items():                           # unpact inner dict
            print(f'          {letter2} : {dict2}    ')                 # Print N : ['name_Surname','name_Surname' ]

#  main()
my_dict=thesaurus_adv(list_names)
print_output(my_dict)

