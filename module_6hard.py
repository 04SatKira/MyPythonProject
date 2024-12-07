import math

class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        self._color = self._validate_color(color)
        self.filled = True
        self.sides = self._set_sides(*sides)

    def _validate_color(self, color):
        try:
            r, g, b = color
            if all(isinstance(c, int) and 0 <= c <= 255 for c in [r, g, b]):
                return [r, g, b]
            else:
                return [0, 0, 0]
        except (ValueError, TypeError):
            return [0, 0, 0]


    def set_color(self, r, g, b):
        new_color = self._validate_color([r, g, b])
        if new_color != [0, 0, 0]:
            self._color = new_color

    def get_color(self):
        return self._color

    def _is_valid_sides(self, *new_sides):
        return all(isinstance(side, (int, float)) and side > 0 for side in new_sides)

    def _set_sides(self, *sides):
        if len(sides) == self.sides_count and self._is_valid_sides(*sides):
            return list(sides)
        elif len(sides) > 0 and sides[0] > 0:
            return [sides[0]] * self.sides_count
        else:
            return [1] * self.sides_count


    def get_sides(self):
        return self.sides

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self._is_valid_sides(*new_sides):
            self.sides = list(new_sides)

    def __len__(self):
        return sum(self.sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        self.radius = self.sides[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.radius**2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        if s <= 0 or s - a <= 0 or s - b <= 0 or s - c <= 0:
            return 0
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)

    def get_volume(self):
        return self.sides[0] ** 3


# Пример использования
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())