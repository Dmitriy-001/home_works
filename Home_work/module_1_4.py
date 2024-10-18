name = input('Ваше имя? ')
current_year = 2024
date_of_birth = input('В каком году Вы родились? ')
age = current_year - int(date_of_birth)
my_string = 'Привет, ' + name + ', Вам в этом году ' + str(age) + ' годиков.'

# в верхнем регистре
print(my_string .upper())

# в нижнем регистре
print(my_string .lower())

# убираем пробелы
print(my_string .replace(' ', ''))

# первый символ строки
first_char = my_string[0]
print(first_char)

# последний символ строки
last_char = my_string[-1]
print(last_char)
