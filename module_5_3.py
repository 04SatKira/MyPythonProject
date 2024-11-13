class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = int(number_of_floor)
    def go_to(self, new_floor):
        floor = 0
        for i in range(1,new_floor + 1):
            if 1 <= new_floor <= self.number_of_floor:
                print(i) 
            else:
                print("Такого этажа не существует")
    def __len__(self):
        return self.number_of_floor
    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floor}')
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floor == other
        elif isinstance(other, int):
            return self.number_of_floor == other
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor < other
        elif isinstance(other, int):
            return self.number_of_floor < other
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floor <= other
        elif isinstance(other, int):
            return self.number_of_floor <= other
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor > other
        elif isinstance(other, int):
            return self.number_of_floor > other
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floor >= other
        elif isinstance(other, int):
            return self.number_of_floor >= other
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floor != other
        elif isinstance(other, int):
            return self.number_of_floor != other
    def __add__(self, value):
        if isinstance(value, House):
            return self.number_of_floor + value
        elif isinstance(value, int):
            return self.number_of_floor + value
    def __iadd__(self, value):
        return self.__add__(value)
    def __radd__(self, value):
        return self.__add__(value)
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2) 
h1.number_of_floor += 10
print(h1)
print(h1 == h2)

h1.number_of_floor = h1.number_of_floor + 10
print(h1)

h2.number_of_floor = 10 + h2.number_of_floor
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

