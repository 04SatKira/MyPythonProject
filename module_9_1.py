def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        try:
            results[func.__name__] = func(int_list)
        except TypeError:
            print(f"Внимание: Функция {func.__name__} не может быть применена к списку ввода.")
            
        except Exception as e:
            print(f"При вводе произошла ошибка {func.__name__}: {e}")

    return results

print(apply_all_func([6, 20, 15, 9], max, min))

print(apply_all_func([6, 20, 15, 9], len, sum, sorted))