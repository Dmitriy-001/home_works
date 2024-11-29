def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Базовый случай: если строка пуста, возвращаем 1
    if len(str_number) == 0:
        return 1

    # Берем первую цифру
    first = int(str_number[0])

    # Если первая цифра 0, пропускаем её и переходим к остальным
    if first == 0:
        return get_multiplied_digits(str_number[1:])

    # Умножаем первую цифру на результат рекурсии для оставшихся символов
    return first * get_multiplied_digits(str_number[1:])


# Пример вызова функции
result = get_multiplied_digits(40203)
print(result)  # Ожидаемый вывод: 24

result2 = get_multiplied_digits(402030)
print(result2)  # Ожидаемый вывод: 24
