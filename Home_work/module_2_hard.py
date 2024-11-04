def generate_password(n):
    result = ""  # Строка для результата

    # Перебираем числа от 1 до n-1 (т.е., исключаем n)
    for i in range(1, n):
        # Внутренний цикл для поиска второй части пары
        for j in range(i + 1, n):
            if (i + j) != 0 and n % (i + j) == 0:
                result += str(i) + str(j)  # Добавляем пару к результату

    return result

# Примеры использования функции
for test_n in range(3, 21):
    print(f"{test_n} - {generate_password(test_n)}")
