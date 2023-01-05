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
# for i in range(10)
#     print(i)
SyntaxError # синтаксическая ошибка

# for i in range(10):
# print(i)
IndentationError # ошибка отступа

# for i in range(10):
        # print(i)
TabError # ошибка табуляции (смешивание табов и пробелов)

# contacts = {
#     'Valera': 996774888333,
#     'Adilet': 996887993002
# }
# contacts['Zaynab']
# print('Hello')
# print(1 + 1)


# try except - конструкция для обработки исключений
# try:
#     contacts = {
#         'Valera': 996774888333,
#         'Adilet': 996887993002
#     }
#     contacts['Azamat']
# except:
#     print('Нет такого имени')
# print('Hello world')
# print(1 + 1)


# try:
#     print('Hello')
#     10 / 0
#     print('World')
# except:
#     print('что-то пошло не так')
# else:
#     print('try работал без ошибок')
# finally:
#     print('я отработаю в любом случае')
"""
Hello
что-то пошло не так
я отработаю в любом случае
"""

nums = [1, 2, 3, 4]
try:
    a = nums[-1]
    a / 0
    nums[10]
except:
    print('Возникла ошибка')

try:
    print(c)
    10 / 0
except (NameError, ZeroDivisionError):
    print('нет такого имени')