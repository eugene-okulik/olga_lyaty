# Общий класс для всех цветов
class Flowers:
    def __init__(self, name, colour, cost, lifespan, stem_length):
        self.name = name                   # Название цветка
        self.colour = colour               # Цвет цветка
        self.cost = cost                   # Стоимость цветка
        self.lifespan = lifespan           # Время жизни цветка в днях
        self.stem_length = stem_length     # Длина стебля в см

    def __repr__(self):
        return (f'{self.name} (colour = {self.colour}, cost = {self.cost}, lifespan = {self.lifespan},' 
                f'stem_length = {self.stem_length})')


# Классы для различных видов цветов
class Rose(Flowers):
    def __init__(self, colour, cost, lifespan, stem_length):
        super().__init__('Rose', colour, cost, lifespan, stem_length)


class Tulip(Flowers):
    def __init__(self, colour, cost, lifespan, stem_length):
        super().__init__('Tulip', colour, cost, lifespan, stem_length)


class Lily(Flowers):
    def __init__(self, colour, cost, lifespan, stem_length):
        super().__init__('Lily', colour, cost, lifespan, stem_length)


class Bouquet:
    def __init__(self):
        self.flowers = []      # Список объектов цветов в букете

    def add_flower(self, flower):
        self.flowers.append(flower)   # Добавление цветка в букет

    def get_total_cost(self):
        return sum(flower.cost for flower in self.flowers)  # Общая стоимость букета

    def get_average_lifespan(self):
        return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)   # Среднее время жизни букета

    def sort_by(self, attribute):
        self.flowers.sort(key=lambda flower: getattr(flower, attribute))

    def find_by_lifespan(self, lifespan):
        return [flower for flower in self.flowers if flower.lifespan == lifespan]

    def find_by_cost(self, cost):
        return [flower for flower in self.flowers if flower.cost == cost]

    def __repr__(self):
        return f"Состав букета: ({self.flowers})"


# Создание объектов цветов разных видов
flouwer_1 = Rose("Pink", 5, 11, 45)
flouwer_2 = Tulip("Yellow", 7, 12, 42)
flouwer_3 = Lily("White", 6, 10, 38)
flouwer_4 = Rose("Purple", 8, 8, 40)

# Создание букета и добавление цветов
bouquet = Bouquet()
bouquet.add_flower(flouwer_1)
bouquet.add_flower(flouwer_2)
bouquet.add_flower(flouwer_3)
bouquet.add_flower(flouwer_4)

# Вывод информации о букете
print('Букет до сортровки:')
print(bouquet)

# Вычисление общей стоимости букета
print('\nСтоимость букета:', bouquet.get_total_cost())

# Вычисление среднего времени жизни букета
print('\nСреднее время жизни букета:', bouquet.get_average_lifespan())

# Сортировка букета по стомости
bouquet.sort_by('cost')
print("\nБукет отсортированный по стоимости:")
print(bouquet)

# Сортировка букета по цвету
bouquet.sort_by('colour')
print("\nБукет отсортированный по цвету:")
print(bouquet)

# Сортировка букета по свежести
bouquet.sort_by('lifespan')
print("\nБукет отсортированный по свежести:")
print(bouquet)

# Сортировка букета по длине стебля
bouquet.sort_by('stem_length')
print("\nБукет отсортированный по длине стебля:")
print(bouquet)

# Поиск цветов по времени жизни
print("\nЦветок с временем жизни 10 дней:")
print(bouquet.find_by_lifespan(10))

# Поиск цветов по стоимости
print("\nЦветок со стоимостью 8 р.:")
print(bouquet.find_by_lifespan(8))
