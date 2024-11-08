# 1st program
result = (9 ** 0.5) * 5
print(result)  # Ожидаемый результат: 15.0

# 2nd program
result = (9.99 > 9.98) and (1000 != 1000.1)
print(result)  # Ожидаемый результат: True

# 3rd program
expression1 = 2 * 2 + 2  # Без приоритета (умножение идет первым)
expression2 = 2 * (2 + 2)  # С приоритетом для сложения
print(expression1)  # Ожидаемый результат: 6
print(expression2)  # Ожидаемый результат: 8
print(expression1 == expression2)  # Ожидаемый результат: False

# 4th program
number_str = '123.456'
number = float(number_str)  # Преобразуем строку в дробное число
shifted_number = number * 10  # Умножаем на 10, чтобы сдвинуть первую цифру после запятой в целую часть
first_digit_after_point = int(shifted_number) % 10  # Извлекаем первую цифру после запятой
print(first_digit_after_point)  # Ожидаемый результат: 4
