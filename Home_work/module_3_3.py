def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызовы функции с разным количеством аргументов
print("Вызов без аргументов:")
print_params()

print("\nВызов с параметром b=25:")
print_params(b=25)

print("\nВызов с параметром c=[1, 2, 3]:")
print_params(c=[1, 2, 3])

# Распаковка параметров
values_list = [42, 'hello', False]
values_dict = {'a': 100, 'b': 'world', 'c': None}

print("\nРаспаковка списка:")
print_params(*values_list)

print("\nРаспаковка словаря:")
print_params(**values_dict)

# Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print("\nРаспаковка списка с добавлением параметра:")
print_params(*values_list_2, 42)
