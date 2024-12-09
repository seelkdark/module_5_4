class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # Создание нового объекта
        instance = super(House, cls).__new__(cls)
        # Добавление названия здания в историю
        if args:  # Проверяем, что переданы аргументы
            cls.houses_history.append(args[0])
        return instance
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return NotImplemented
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return True
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        return NotImplemented
    def __radd__(self, value):
        return self.__add__(value)
    def __iadd__(self, value):
        return self.__add__(value)
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    def __len__(self):
        return self.number_of_floors


# Пример использования класса
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # ['ЖК Эльбрус']
h2 = House('ЖК Акация', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2  # Вывод: ЖК Акация снесён, но он останется в истории
del h3  # Вывод: ЖК Матрёшки снесён, но он останется в истории

print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']