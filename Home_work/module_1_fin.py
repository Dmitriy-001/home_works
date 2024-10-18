# grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# # Преобразуем множество students в список, чтобы сохранить порядок
# students_list = sorted(students)  # сортируем для соответствия алфавитному порядку оценок
#
# # Создаем пустой словарь для хранения результатов
# average_grades = {}
#
# # Заполняем словарь, используя имена и оценки
# for i in range(len(students_list)):
#     average_grades[students_list[i]] = sum(grades[i]) / len(grades[i])
#
# # Выводим результат
# print(average_grades)


# # Исходные данные
# grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# # Шаг 1: Преобразуем множество студентов в отсортированный список для сохранения порядка
# # Сортируем по алфавиту, чтобы соответствовать порядку оценок
# students_list = sorted(students)
# print(f"Отсортированный список студентов: {students_list}")
# # -> Отсортированный список студентов: ['Aaron', 'Bilbo', 'Johnny', 'Khendrik', 'Steve']
#
# # Шаг 2: Создаем пустой словарь для хранения среднего балла каждого студента
# average_grades = {}
#
# # Шаг 3: Проходим по всем элементам отсортированного списка студентов
# for i in range(len(students_list)):
#     # Получаем имя студента по индексу i
#     student_name = students_list[i]
#
#     # Получаем список оценок для этого студента по индексу i
#     student_grades = grades[i]
#
#     # Рассчитываем сумму всех оценок студента
#     total_grades = sum(student_grades)
#
#     # Узнаем количество оценок у студента
#     num_of_grades = len(student_grades)
#
#     # Рассчитываем средний балл (сумма оценок деленная на их количество)
#     average_grade = total_grades / num_of_grades
#
#     # Добавляем запись в словарь: ключ — имя студента, значение — его средний балл
#     average_grades[student_name] = average_grade
#
#     # Подробный вывод на каждом этапе
#     print(f"Студент: {student_name}")
#     print(f"Оценки: {student_grades}")
#     print(f"Сумма оценок: {total_grades}")
#     print(f"Количество оценок: {num_of_grades}")
#     print(f"Средний балл: {average_grade}")
#     print("-" * 40)  # Разделитель для наглядности
#
# # Шаг 4: Выводим итоговый словарь со средними баллами всех студентов
# print("Итоговый словарь со средними баллами:")
# print(average_grades)


# # Исходные данные
# grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# # Преобразуем множество студентов в отсортированный список
# students_list = sorted(students)
# print(f"Отсортированный список студентов: {students_list}")
#
# # Создаем пустой словарь для хранения среднего балла
# average_grades = {}
#
# # Проходим по именам студентов и их оценкам одновременно с помощью zip()
# for student_name, student_grades in zip(students_list, grades):
#     # Рассчитываем сумму всех оценок студента
#     total_grades = sum(student_grades)
#
#     # Узнаем количество оценок у студента
#     num_of_grades = len(student_grades)
#
#     # Рассчитываем средний балл
#     average_grade = total_grades / num_of_grades
#
#     # Добавляем запись в словарь: имя студента -> средний балл
#     average_grades[student_name] = average_grade
#
#     # Подробный вывод
#     print(f"Студент: {student_name}")
#     print(f"Оценки: {student_grades}")
#     print(f"Сумма оценок: {total_grades}")
#     print(f"Количество оценок: {num_of_grades}")
#     print(f"Средний балл: {average_grade}")
#     print("-" * 30)
#
# # Вывод итогового словаря
# print("Итоговый словарь со средними баллами:")
# print(average_grades)


print("Python-лучше всех!")
print('Кошка сказала "мяу".')