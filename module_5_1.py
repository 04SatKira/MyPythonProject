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
                break
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
