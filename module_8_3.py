class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        try:
            self.__vin = self.__is_valid_vin(vin)
        except IncorrectVinNumber as e:
            print(e.message)
            self.__vin = None # или другое значение по умолчанию

        try:
            self.__numbers = self.__is_valid_numbers(numbers)
        except IncorrectCarNumbers as e:
            print(e.message)
            self.__numbers = None # или другое значение по умолчанию


    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return vin_number

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return numbers


first = Car('Model1', 1000000, 'f123dj')
if first.__vin and first.__numbers:
    print(f'{first.model} успешно создан')


second = Car('Model2', 300, 'т001тр')
if second.__vin and second.__numbers:
    print(f'{second.model} успешно создан')


third = Car('Model3', 2020202, 'нет номера')
if third.__vin and third.__numbers:
    print(f'{third.model} успешно создан')