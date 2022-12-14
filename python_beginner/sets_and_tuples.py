""" Множества (set) """

# set()

# set - изменяемая, неупорядоченная, итерируемая последовательность, которая содержит уникальные/неповторяющиеся и неизменяемые элементы

# коллекции - типы данных, которые могут содержать в себе последовательность элементов (list, tuple, dict, set)

# литералы - {}

# my_set = {1, 'string', 2, 3}
# print(my_set)

# my_set2 = {'h', 'k', 'a', 'b'}
# print(my_set2)

# my_set3 = {1, 2, 3, 1, 3, 4, 4}
# print(my_set3)

# удаление дубликатов
# list_of_names = ['Alena', 'Aliya', 'Alena', 'Misha', 'Kayrat', 'Kayrat']
# print(list(set(list_of_names)))


# empty_set = {} # это не set, а dict
# print(type(empty_set))

# real_empty_set = set()
# print(type(real_empty_set))


""" Методы сетов """
# class_js = {'Aktan', 'Aygul', 'Mayrash', 'Artyom'}
# class_python = {'Malik', 'Aygul', 'Eldos', 'Aktan'}

# inter = class_js.intersection(class_python)
# print(class_js & class_python)
# print(inter)

# diff = class_js.difference(class_python)
# diff2 = class_python.difference(class_js)
# print(class_js - class_python)
# print(diff)
# print(diff2)

# print(class_js.union(class_python))
# print(class_js | class_python)

# fruits = {'apple', 'banana', 'kiwi', 'tangerine'}
# vegetables = {'carrot', 'potato', 'tomato', 'apple'}

# fruits.intersection_update(vegetables)
# print(fruits)

# fruits.difference_update(vegetables)
# vegetables.difference_update(fruits)
# print(fruits)
# print(vegetables)


# a = {1, 2, 3, ['a', 'b']} # TypeError

# my_unique_set = {1, 'string', True, False, 0, (1, 2)}
# print(my_unique_set) # {False, 1, (1, 2), 'string'}

""" Кортеж (tuple) """

# tuple()

# кортеж - неизменяемый, итерируемый, индекстируемый, упорядоченный тип данных

# литералы - ()

# tuple1 = (1, 2, 3, 4, [1, 2])
# tuple2 = 1, 2, 3, 4, [1, 2]
# print(type(tuple1))
# print(type(tuple2))

# t1 = ('1 element', )
# print(type(t1))
# t2 = '2 element', 
# print(type(t2))

# a, b, c = (1, 2, 3)
# звездочный синтаксис
# tuple_of_nums = tuple(range(5))
# print(*tuple_of_nums)
# print(0, 1, 2, 3, 4)

# tuple_of_nums = (0, 1, 2, 3)
# v1, *v2, v3 = tuple_of_nums
# print(v1)
# print(v2)
# print(v3)


# human = ['heart', 'eyea', 'hands']
# human[1] = 'wheels'
# print(human)

# human = ('heart', 'eyea', 'hands')
# human[1] = 'wheels'

# l1 = [1, 2, 3]
# t1 = (1, 2, 3)
# print(l1.__sizeof__())
# print(t1.__sizeof__())


# s1 = {'string', 'string2', {1, 2, 3}}
# print(hash('string'))
# {7385479864691161137: 'string'}

t1 = (1, 2, 3)
# l1 = (3, 4, 5)
# pow(*t1)
# pow(t1[0], t1[1], t1[2])
# pow(*l1)

# print(dir(t1))

# t2 = (1, 2, 3, 3, 3)
# print(t2.count(3))
# print(t2.index(2))

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# new_tuple = tuple1 + tuple2
# print(new_tuple)