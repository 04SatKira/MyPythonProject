def all_variants(text):
    """
    Функция-генератор, которая возвращает все подпоследовательности переданной строки.
    """
    n = len(text)
    for i in range(n):
        yield text[i]  # Отдельные символы

    for i in range(n - 1):
        for j in range(i + 1, n):
            yield text[i:j+1] # Подпоследовательности длиной больше 1


# Пример использования:
a = all_variants("abc")

for i in a:
    print(i)