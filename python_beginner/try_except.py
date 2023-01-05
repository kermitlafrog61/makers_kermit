""" try except - ошибки и исключения в python """

# исклбение - проблема в логике работы кода
# ошибка - проблема в написании кода/синтаксисе кода

# исключения можно обработать выловить и обработать. Ошибки - нельзя

# a = 10
# b = 20
# print(c)
NameError # исключение отсутсвия имени

# 10 / 0
ZeroDivisionError # исключение при делении на ноль

# names = {'Misha': 20, 'Nur': 30}
# names['Azamat']
KeyError # исключение ключа

# list_ = [1, 2, 3]
# list_[5]
IndexError # индекс не входит в диапозон списка

# num = 10
# num + 'string'
TypeError # ошибка типов данных, когда тип объекта не подходит для операции

int(10) # ok
int(10.1) # ok
int('20') # ok
# int('sting')
# from math import sqrt
# sqrt(25) # ok
# sqrt(-20) # ValueError
ValueError # ошибка значения. Кргда тип объекта подходит под условие, но его значение - нет 

string = 'hello world'
# string.append('b')
AttributeError # отсутствие атрибута или метода у объекта

# import wrong_module
ModuleNotFoundError
# from math import wrong_func
ImportError

# ошибки
for i in range(10)
    print(i)











