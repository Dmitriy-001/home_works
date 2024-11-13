# Глобальная переменная для подсчета вызовов
calls = 0

# Функция для подсчета вызовов
def count_calls():
    global calls
    calls += 1

# Функция для анализа строки
def string_info(string):
    count_calls()  # Увеличиваем счетчик вызовов
    return (len(string), string.upper(), string.lower())

# Функция для проверки наличия строки в списке с игнорированием регистра
def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    string_lower = string.lower()
    list_lower = [item.lower() for item in list_to_search]
    return string_lower in list_lower

# Тестирование функций с произвольными данными
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))    # No matches

# Вывод количества вызовов
print(calls)
