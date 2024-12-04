def calculate_structure_sum(*args):
    total_sum = 0

    def recursive_sum(element):
        nonlocal total_sum

        if isinstance(element, int):  # Если элемент — число
            total_sum += element
        elif isinstance(element, str):  # Если элемент — строка
            total_sum += len(element)
        elif isinstance(element, (list, tuple, set)):  # Если элемент — коллекция
            for item in element:
                recursive_sum(item)
        elif isinstance(element, dict):  # Если элемент — словарь
            for key, value in element.items():
                recursive_sum(key)
                recursive_sum(value)

    for arg in args:  # Обрабатываем каждый аргумент
        recursive_sum(arg)

    return total_sum
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Вывод: 99