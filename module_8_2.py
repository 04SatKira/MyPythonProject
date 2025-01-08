def personal_sum(numbers):
    """
    Подсчитывает сумму чисел в коллекции, игнорируя нечисловые данные и выводя сообщения об ошибках.

    Args:
        numbers: Коллекция чисел.

    Returns:
        Кортеж (сумма, количество некорректных данных).
    """
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчёта суммы - {number}")
    return result, incorrect_data


def calculate_average(numbers):
    """
    Вычисляет среднее арифметическое чисел в коллекции.

    Args:
        numbers: Коллекция чисел.

    Returns:
        Среднее арифметическое или 0 в случае пустой коллекции, или None в случае некорректного типа данных.
    """
    try:
        iter(numbers)
    except TypeError:
        return "В numbers записан некорректный тип данных"

    total, incorrect = personal_sum(numbers)
    if len(numbers) - incorrect == 0:
        return 0
    return total / (len(numbers) - incorrect)


# Тесты
print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')