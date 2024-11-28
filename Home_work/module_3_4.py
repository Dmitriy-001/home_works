def single_root_words(root_word, *other_words):
    same_words = []

    # Приводим root_word к нижнему регистру для сравнения без учета регистра
    root_word_lower = root_word.lower()

    for word in other_words:
        if root_word_lower in word.lower() or word.lower() in root_word_lower:
            same_words.append(word)

    return same_words


# Пример вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Вывод результатов
print(result1)  # ['richiest', 'orichalcum', 'richies']
print(result2)  # ['Able', 'Disable']
