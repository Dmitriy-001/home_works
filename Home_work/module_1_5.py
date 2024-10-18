immutable_var = (42, 3.14, 'Python', True, [1, 2, 3])
print(immutable_var)

# Попытаемся изменить первый элемент кортежа
# immutable_var[0] = 100

# Это происходит потому, что кортежи в Python
# являются неизменяемыми (immutable) структурами данных.
# Это означает, что после создания кортежа нельзя изменить
# его элементы напрямую — ни заменить значения, ни добавить,
# ни удалить их.

# Создаем переменную mutable_list и присваиваем ей список из нескольких элементов
mutable_list = [1, True, 3, 4, 5]
print(mutable_list)
# Изменяем элементы списка
mutable_list[1] = 10
mutable_list[2] = 30

# Выводим измененный список на экран
print(mutable_list)
