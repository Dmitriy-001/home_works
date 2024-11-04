def get_matrix(n, m, value):
    # Проверяем, чтобы значения n и m были положительными
    if n <= 0 or m <= 0:
        return []  # Возвращаем пустой список, если n или m меньше или равны 0

    # Создаем пустую матрицу
    matrix = []

    # Заполняем матрицу
    for i in range(n):  # Внешний цикл для строк
        row = []  # Создаем пустую строку
        for j in range(m):  # Внутренний цикл для столбцов
            row.append(value)  # Заполняем строку значениями value
        matrix.append(row)  # Добавляем строку в матрицу

    return matrix


# Примеры вызова функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Вывод результатов на экран
print(result1)
print(result2)
print(result3)
